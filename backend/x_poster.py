"""
X (Twitter) posting bot — free API tier (v2).

Free tier limits (as of 2025):
  - 1,500 Posts/month  → ~50/day budget (we default to 17 to be safe)

Posting strategy:
  1. Try tweepy (works on Python ≤ 3.12, used by GitHub Actions / Python 3.11)
  2. Fall back to direct X API v2 via requests-oauthlib (works on Python 3.13+,
     used by Streamlit Cloud which runs Python 3.14)
  This means tweepy is NEVER imported at module level — so importing this file
  on Python 3.14 no longer crashes with "No module named 'imghdr'".

Post format examples:
  👀 Patrick Mahomes (@patrickmahomes) just followed @someaccount on Instagram
  Patrick Mahomes (@patrickmahomes) unfollowed @someaccount on Instagram
"""
import os
import logging

from backend import database as db

logger = logging.getLogger(__name__)

_X_TWEET_URL = "https://api.twitter.com/2/tweets"


# ── Credential helpers ────────────────────────────────────────────────────

def _check_x_credentials():
    required = [
        "X_API_KEY", "X_API_KEY_SECRET",
        "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET",
    ]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        raise EnvironmentError(
            f"Missing X API credentials: {', '.join(missing)}"
        )


# ── Low-level tweet posting ───────────────────────────────────────────────

def _post_tweet(text: str) -> str:
    """
    Post one tweet and return the tweet ID string.
    Tries tweepy (Python ≤3.12) then falls back to requests-oauthlib
    direct call (Python 3.13+/3.14).
    """
    _check_x_credentials()

    # ── Path 1: tweepy (GitHub Actions, Python 3.11) ──────────────────
    try:
        import tweepy  # noqa: PLC0415 — intentionally lazy
        client = tweepy.Client(
            consumer_key=os.environ["X_API_KEY"],
            consumer_secret=os.environ["X_API_KEY_SECRET"],
            access_token=os.environ["X_ACCESS_TOKEN"],
            access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
        )
        response = client.create_tweet(text=text)
        return str(response.data["id"])
    except ImportError:
        pass  # Python 3.13+ removed imghdr; tweepy 4.14 can't be imported

    # ── Path 2: direct X API v2 via requests-oauthlib (Streamlit Cloud) ─
    try:
        from requests_oauthlib import OAuth1Session  # noqa: PLC0415
    except ImportError as exc:
        raise RuntimeError(
            "Neither tweepy nor requests-oauthlib is available. "
            "Add requests-oauthlib to requirements.txt."
        ) from exc

    oauth = OAuth1Session(
        os.environ["X_API_KEY"],
        client_secret=os.environ["X_API_KEY_SECRET"],
        resource_owner_key=os.environ["X_ACCESS_TOKEN"],
        resource_owner_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )
    resp = oauth.post(_X_TWEET_URL, json={"text": text})
    if resp.status_code == 429:
        raise RuntimeError("429 TooManyRequests")
    if not resp.ok:
        raise RuntimeError(f"X API {resp.status_code}: {resp.text[:300]}")
    return str(resp.json()["data"]["id"])


# ── Tweet text formatting ─────────────────────────────────────────────────

def _format_tweet(event: dict) -> str:
    player     = event["player_name"]
    player_ig  = f"@{event['player_ig_handle']}"
    target     = f"@{event['ig_username']}"
    full_name  = event.get("ig_full_name", "")
    display    = (
        f"{full_name} ({target})"
        if full_name and full_name != event["ig_username"]
        else target
    )
    hashtag = _team_hashtag(event.get("team", ""))

    if event["event_type"] == "follow":
        return (
            f"\U0001f440 {player} ({player_ig}) just followed "
            f"{display} on Instagram\n#NFL #{hashtag}"
        ).strip()
    else:
        return (
            f"{player} ({player_ig}) unfollowed "
            f"{display} on Instagram\n#NFL #{hashtag}"
        ).strip()


def _team_hashtag(team: str) -> str:
    return team.replace(" ", "").replace(".", "") if team else "NFL"


# ── Public API ────────────────────────────────────────────────────────────

def post_pending_events(dry_run: bool = False) -> int:
    """
    Fetch unposted events and post them to X, respecting the daily cap.
    Returns the number of posts made (or marked for dry_run).
    """
    max_per_day  = int(os.environ.get("MAX_X_POSTS_PER_DAY", "17"))
    posted_today = db.count_x_posts_today()
    remaining    = max_per_day - posted_today

    if remaining <= 0:
        logger.info(f"Daily X post limit reached ({max_per_day}). Skipping.")
        return 0

    events = db.get_unposted_events(limit=remaining)
    if not events:
        logger.info("No unposted events to tweet.")
        return 0

    if not dry_run:
        try:
            _check_x_credentials()
        except EnvironmentError as e:
            logger.warning(f"X credentials not configured: {e}")
            return 0

    posted_count = 0
    for event in events:
        tweet_text = _format_tweet(event)

        if dry_run:
            logger.info(f"[DRY RUN] Would tweet:\n{tweet_text}")
            db.mark_event_posted(event["id"], x_post_id="dry_run")
            posted_count += 1
            continue

        try:
            tweet_id = _post_tweet(tweet_text)
            db.mark_event_posted(event["id"], x_post_id=tweet_id)
            logger.info(f"Posted tweet {tweet_id}: {tweet_text[:60]}…")
            posted_count += 1
        except RuntimeError as e:
            if "429" in str(e) or "TooManyRequests" in str(e):
                logger.warning("X rate limit hit. Stopping for now.")
                break
            logger.error(f"Tweet failed for event {event['id']}: {e}")
        except Exception as e:
            logger.error(f"Tweet failed for event {event['id']}: {e}")

    logger.info(
        f"X posting done: {posted_count} new posts "
        f"({posted_today + posted_count}/{max_per_day} today)"
    )
    return posted_count


def preview_pending_tweets() -> list[dict]:
    """
    Return formatted tweet previews for all pending unposted events.
    Nothing is posted or marked — purely read-only.
    Used by the Streamlit admin panel.
    """
    max_per_day  = int(os.environ.get("MAX_X_POSTS_PER_DAY", "17"))
    posted_today = db.count_x_posts_today()
    remaining    = max_per_day - posted_today

    events   = db.get_unposted_events(limit=50)
    previews = []
    for i, event in enumerate(events):
        previews.append({
            "tweet":       _format_tweet(event),
            "event_id":    event["id"],
            "player":      event.get("player_name", ""),
            "event_type":  event.get("event_type", ""),
            "would_post":  i < remaining,
        })
    return previews
