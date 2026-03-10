#!/usr/bin/env bash
# Convenience script to start both the scheduler and web server.
# Usage:  ./run.sh [web|scheduler|both]

set -e

MODE="${1:-both}"

source venv/bin/activate 2>/dev/null || true

case "$MODE" in
  web)
    echo "Starting web server on http://0.0.0.0:${FLASK_PORT:-5000}"
    python -m backend.app
    ;;
  scheduler)
    echo "Starting tracker scheduler (interval: ${CHECK_INTERVAL_HOURS:-6}h)"
    python -m backend.scheduler
    ;;
  seed)
    python -m backend.scheduler --seed
    ;;
  once)
    python -m backend.scheduler --once
    ;;
  both)
    echo "Starting scheduler in background + web server in foreground…"
    python -m backend.scheduler &
    SCHED_PID=$!
    trap "kill $SCHED_PID 2>/dev/null" EXIT
    python -m backend.app
    ;;
  *)
    echo "Usage: $0 [web|scheduler|both|seed|once]"
    exit 1
    ;;
esac
