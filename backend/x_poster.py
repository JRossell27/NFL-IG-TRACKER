"""
X (Twitter) posting bot using Tweepy v4 with the free API tier.

Free tier limits (as of 2025):
  - 1,500 Posts/month  → ~50/day budget (we default to 17 to be safe)

Post format examples:
  👀 Patrick Mahomes (@patrickmahomes) just followed @someaccount on Instagram
  Patrick Mahomes (@patrickmahomes) unfollowed @someaccount on Instagram
"""
import os
import logging
from datetime import datetime, timezone

import tweepy

from backend import database as db

logger = logging.getLogger(__name__)


def _get_client() -> tweepy.Client:
    required = [
        "X_API_KEY", "X_API_KEY_SECRET",
        "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET",
    ]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        raise EnvironmentError(
            f"Missing X API credentials: {', '.join(missing)}"
        )
    return tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_KEY_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )


def _format_tweet(event: dict) -> str:
    """Build tweet text for a follow/unfollow event."""
    player = event["player_name"]
    player_ig = f"@{event['player_ig_handle']}"
    target = f"@{event['ig_username']}"
    full_name = event.get("ig_full_name", "")
    display_target = f"{full_name} ({target})" if full_name and full_name != event["ig_username"] else target

    if event["event_type"] == "follow":
        return (
            f"\U0001f440 {player} ({player_ig}) just followed "
            f"{display_target} on Instagram\n#NFL #{_team_hashtag(event.get('team',''))}"
        ).strip()
    else:
        return (
            f"{player} ({player_ig}) unfollowed "
            f"{display_target} on Instagram\n#NFL #{_team_hashtag(event.get('team',''))}"
        ).strip()


def _team_hashtag(team: str) -> str:
    """Convert team name to a hashtag-friendly string."""
    return team.replace(" ", "").replace(".", "") if team else "NFL"


def post_pending_events(dry_run: bool = False) -> int:
    """
    Fetch unposted events and post them to X, respecting the daily cap.
    Returns the number of posts made.
    """
    max_per_day = int(os.environ.get("MAX_X_POSTS_PER_DAY", "17"))
    posted_today = db.count_x_posts_today()
    remaining = max_per_day - posted_today

    if remaining <= 0:
        logger.info(f"Daily X post limit reached ({max_per_day}). Skipping.")
        return 0

    events = db.get_unposted_events(limit=remaining)
    if not events:
        logger.info("No unposted events to tweet.")
        return 0

    client = None
    if not dry_run:
        try:
            client = _get_client()
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
            response = client.create_tweet(text=tweet_text)
            tweet_id = str(response.data["id"])
            db.mark_event_posted(event["id"], x_post_id=tweet_id)
            logger.info(f"Posted tweet {tweet_id}: {tweet_text[:60]}…")
            posted_count += 1
        except tweepy.errors.TooManyRequests:
            logger.warning("X rate limit hit. Stopping for now.")
            break
        except tweepy.errors.TweepyException as e:
            logger.error(f"Tweet failed for event {event['id']}: {e}")
            # Don't break – try next event

    logger.info(f"X posting done: {posted_count} new posts ({posted_today + posted_count}/{max_per_day} today)")
    return posted_count
