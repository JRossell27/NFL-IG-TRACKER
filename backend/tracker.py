"""
Instagram following tracker using instagrapi (unofficial Instagram private API).

Usage:
    tracker = InstagramTracker()
    tracker.login()
    tracker.check_player(player_id)
    tracker.logout()
"""
import os
import json
import time
import random
import logging
from pathlib import Path

from instagrapi import Client
from instagrapi.exceptions import (
    LoginRequired, UserNotFound, ClientError, RateLimitError
)

from backend import database as db

logger = logging.getLogger(__name__)

SESSION_FILE = Path(__file__).parent / "session.json"


class InstagramTracker:
    def __init__(self):
        self.cl = Client()
        self.cl.delay_range = [2, 5]   # seconds between requests
        self._logged_in = False

    # ------------------------------------------------------------------
    # Auth
    # ------------------------------------------------------------------

    def login(self):
        username = os.environ.get("INSTAGRAM_USERNAME")
        password = os.environ.get("INSTAGRAM_PASSWORD")
        if not username or not password:
            raise EnvironmentError(
                "INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD must be set."
            )

        if SESSION_FILE.exists():
            try:
                self.cl.load_settings(SESSION_FILE)
                self.cl.login(username, password)
                logger.info("Logged in via saved session.")
                self._logged_in = True
                return
            except Exception as e:
                logger.warning(f"Session reload failed ({e}), re-logging in.")

        self.cl.login(username, password)
        self.cl.dump_settings(SESSION_FILE)
        logger.info("Logged in fresh and saved session.")
        self._logged_in = True

    def logout(self):
        if self._logged_in:
            try:
                self.cl.logout()
            except Exception:
                pass
            self._logged_in = False

    # ------------------------------------------------------------------
    # Player IG user ID resolution
    # ------------------------------------------------------------------

    def resolve_player_ig_id(self, player: dict) -> str | None:
        """Look up and store the numeric Instagram user ID for a player."""
        if player.get("ig_user_id"):
            return player["ig_user_id"]
        try:
            info = self.cl.user_info_by_username(player["ig_handle"])
            uid = str(info.pk)
            db.set_player_ig_user_id(player["id"], uid)
            logger.info(f"Resolved IG user ID for {player['name']}: {uid}")
            return uid
        except UserNotFound:
            logger.warning(f"Instagram user not found: {player['ig_handle']}")
            return None
        except Exception as e:
            logger.error(f"Error resolving IG user ID for {player['name']}: {e}")
            return None

    # ------------------------------------------------------------------
    # Core check
    # ------------------------------------------------------------------

    def check_player(self, player_id: int) -> tuple[list, list]:
        """
        Fetch the player's current following list, diff against stored state,
        record events, and return (follows_added, follows_removed).
        """
        player = db.get_player_by_id(player_id)
        if not player:
            raise ValueError(f"Player {player_id} not found in DB")

        ig_user_id = self.resolve_player_ig_id(player)
        if not ig_user_id:
            return [], []

        logger.info(f"Checking following for {player['name']} (@{player['ig_handle']})")

        # Fetch full following list
        try:
            following_raw = self._fetch_following(ig_user_id)
        except RateLimitError:
            logger.warning(f"Rate limited while fetching following for {player['name']}. Skipping.")
            return [], []
        except LoginRequired:
            logger.error("Login required – session expired.")
            raise
        except Exception as e:
            logger.error(f"Error fetching following for {player['name']}: {e}")
            return [], []

        # Convert to our format
        new_following = {
            str(uid): {
                "ig_username": user.username,
                "ig_full_name": user.full_name,
                "ig_profile_pic": str(user.profile_pic_url) if user.profile_pic_url else None,
            }
            for uid, user in following_raw.items()
        }

        logger.info(f"  {player['name']} follows {len(new_following)} accounts")

        # Diff and persist
        added, removed = db.update_following_snapshot(player_id, new_following)

        # Record events
        for item in added:
            db.record_follow_event(
                player_id=player_id,
                event_type="follow",
                ig_username=item["ig_username"],
                ig_user_id=item["ig_user_id"],
                ig_full_name=item.get("ig_full_name"),
                ig_profile_pic=item.get("ig_profile_pic"),
            )
            logger.info(f"  + FOLLOW: {item['ig_username']}")

        for item in removed:
            db.record_follow_event(
                player_id=player_id,
                event_type="unfollow",
                ig_username=item["ig_username"],
                ig_user_id=item["ig_user_id"],
                ig_full_name=item.get("ig_full_name"),
                ig_profile_pic=item.get("ig_profile_pic"),
            )
            logger.info(f"  - UNFOLLOW: {item['ig_username']}")

        return added, removed

    def _fetch_following(self, ig_user_id: str) -> dict:
        """
        Fetch the complete following list. instagrapi paginates automatically.
        Returns dict of {pk: UserShort}.
        """
        return self.cl.user_following(ig_user_id, amount=0)

    # ------------------------------------------------------------------
    # Batch check all players
    # ------------------------------------------------------------------

    def check_all_players(self, delay_between: tuple = (10, 30)) -> dict:
        """
        Check all active players sequentially with random delays.
        Returns summary dict.
        """
        players = db.get_all_players(active_only=True)
        results = {"checked": 0, "follows": 0, "unfollows": 0, "errors": 0}

        for i, player in enumerate(players):
            try:
                added, removed = self.check_player(player["id"])
                results["checked"] += 1
                results["follows"] += len(added)
                results["unfollows"] += len(removed)
            except LoginRequired:
                logger.error("Session expired mid-run. Re-logging in.")
                try:
                    self.login()
                    added, removed = self.check_player(player["id"])
                    results["checked"] += 1
                    results["follows"] += len(added)
                    results["unfollows"] += len(removed)
                except Exception as e:
                    logger.error(f"Re-login failed: {e}")
                    results["errors"] += 1
                    break
            except Exception as e:
                logger.error(f"Failed checking {player['name']}: {e}")
                results["errors"] += 1

            # Random delay between players to stay under radar
            if i < len(players) - 1:
                sleep_time = random.uniform(*delay_between)
                logger.debug(f"Sleeping {sleep_time:.1f}s before next player…")
                time.sleep(sleep_time)

        logger.info(
            f"Check complete: {results['checked']} players, "
            f"+{results['follows']} follows, -{results['unfollows']} unfollows, "
            f"{results['errors']} errors"
        )
        return results
