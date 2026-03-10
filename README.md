# NFL IG Tracker

Automated Instagram follow/unfollow tracker for NFL players, with:
- **X (Twitter) bot** — posts notable activity (free tier, ≤17 posts/day)
- **Website companion** — search players, browse full follow/unfollow history

---

## How it Works

1. A scheduler runs every 6 hours and fetches each player's Instagram following list via `instagrapi` (unofficial Instagram API).
2. New follows/unfollows are detected by diffing the current list against the stored snapshot.
3. Events are saved to a local SQLite database.
4. The X bot posts the most interesting events (respecting the free-tier daily cap).
5. The Flask web app serves the companion website where anyone can search players and browse full history — no daily limit.

---

## Setup

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env with your credentials
```

Required credentials:
- `INSTAGRAM_USERNAME` / `INSTAGRAM_PASSWORD` — a throwaway IG account used for scraping
- `X_API_KEY`, `X_API_KEY_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` — from [developer.twitter.com](https://developer.twitter.com) (free tier)

### 3. Seed the player database

```bash
python -m backend.scheduler --seed
```

### 4. Run a one-off tracking check

```bash
python -m backend.scheduler --once
```

### 5. Start the scheduler (continuous)

```bash
python -m backend.scheduler
```

### 6. Start the web server (separate terminal)

```bash
python -m backend.app
# Open http://localhost:5000
```

---

## Project Structure

```
NFL-IG-TRACKER/
├── backend/
│   ├── __init__.py
│   ├── database.py      # SQLite schema & all DB operations
│   ├── nfl_players.py   # Seed data: ~70 NFL players with IG handles
│   ├── tracker.py       # Instagram following tracker (instagrapi)
│   ├── x_poster.py      # X posting bot (tweepy)
│   ├── app.py           # Flask REST API + static file server
│   └── scheduler.py     # APScheduler entry point
├── frontend/
│   ├── index.html       # SPA shell
│   ├── styles.css       # Dark NFL-themed styles
│   └── app.js           # Vanilla JS frontend
├── data/                # SQLite DB (git-ignored)
├── logs/                # Log files (git-ignored)
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/players` | List all players (supports `?search=`) |
| GET | `/api/players/:id` | Single player detail |
| GET | `/api/players/:id/events` | Follow/unfollow events for a player |
| GET | `/api/players/:id/following` | Current following list for a player |
| GET | `/api/events/recent` | Recent events across all players |
| GET | `/api/stats` | Aggregate counts |

All endpoints support `?type=follow` or `?type=unfollow` filter and `?limit=` (max 200).

---

## X Post Limits

The free X API tier allows **1,500 writes/month** (~50/day). We default to **17/day** to stay comfortably under, matching the typical free account post limit.

Set `MAX_X_POSTS_PER_DAY` in `.env` to adjust.

---

## Adding / Updating Players

Edit `backend/nfl_players.py` and re-run `--seed`. The upsert is safe to run multiple times.

---

## Notes

- Instagram handles change — verify them periodically.
- `instagrapi` uses Instagram's private mobile API. Use a dedicated throwaway account.
- The first run fetches each player's full following list as a baseline; no events are recorded until the second run.
