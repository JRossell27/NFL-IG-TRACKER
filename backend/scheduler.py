"""
Main scheduler — runs the Instagram tracker and X poster on a schedule.

Usage:
    python -m backend.scheduler             # runs the scheduler loop
    python -m backend.scheduler --once      # single check, then exit
    python -m backend.scheduler --seed      # seed the DB, then exit
    python -m backend.scheduler --post-dry  # dry-run X posting, then exit

Secrets are loaded in this priority order:
  1. Environment variables already set (e.g. GitHub Actions secrets)
  2. .streamlit/secrets.toml  (local dev matching Streamlit setup)
  3. .env file
"""
import os
import sys
import logging
from datetime import datetime, timezone
from pathlib import Path


def _load_secrets():
    """Load credentials from .streamlit/secrets.toml then .env (both optional)."""
    # Try .streamlit/secrets.toml first
    secrets_file = Path(__file__).parent.parent / '.streamlit' / 'secrets.toml'
    if secrets_file.exists():
        try:
            try:
                import tomllib
            except ImportError:
                import tomli as tomllib  # pip install tomli on Python < 3.11
            with open(secrets_file, 'rb') as f:
                secrets = tomllib.load(f)
            for k, v in secrets.items():
                if isinstance(v, str):
                    os.environ.setdefault(k, v)
        except Exception as e:
            print(f"Warning: could not parse secrets.toml: {e}")

    # Also load .env (values already in env take priority via setdefault above)
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass


_load_secrets()

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from backend.database import init_db
from backend.nfl_players import seed_players
from backend.tracker import InstagramTracker
from backend.x_poster import post_pending_events

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def run_tracking_job():
    """Full Instagram check + X posting cycle."""
    logger.info("=" * 60)
    logger.info(f"Starting tracking job at {datetime.now(timezone.utc).isoformat()}")

    tracker = InstagramTracker()
    try:
        tracker.login()
        results = tracker.check_all_players()
        logger.info(f"Tracking results: {results}")
    except Exception as e:
        logger.error(f"Tracking job failed: {e}", exc_info=True)
    finally:
        tracker.logout()

    # Post new events to X
    try:
        posted = post_pending_events()
        logger.info(f"Posted {posted} events to X.")
    except Exception as e:
        logger.error(f"X posting failed: {e}", exc_info=True)

    logger.info("Tracking job complete.")


def main():
    args = sys.argv[1:]

    init_db()  # no-op for Supabase, keeps interface consistent

    if '--seed' in args:
        seed_players()
        return

    if '--post-dry' in args:
        post_pending_events(dry_run=True)
        return

    if '--once' in args:
        run_tracking_job()
        return

    # Continuous scheduler
    interval_hours = int(os.environ.get('CHECK_INTERVAL_HOURS', '6'))
    logger.info(f"Starting scheduler — checking every {interval_hours} hour(s).")
    logger.info("Run with --seed first if you haven't seeded the player list.")

    scheduler = BlockingScheduler(timezone='UTC')
    scheduler.add_job(
        run_tracking_job,
        trigger=IntervalTrigger(hours=interval_hours),
        id='track_and_post',
        name='Instagram tracking + X posting',
        replace_existing=True,
        # Run immediately on startup too
        next_run_time=datetime.now(timezone.utc),
    )

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")


if __name__ == '__main__':
    main()
