"""
Database module: SQLite schema definition and all CRUD operations.
"""
import sqlite3
import os
from datetime import datetime, timezone
from contextlib import contextmanager

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'tracker.db')


def get_db_path():
    path = os.environ.get('DB_PATH', DB_PATH)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    return path


@contextmanager
def get_connection():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    """Create all tables if they don't exist."""
    with get_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS players (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                name        TEXT NOT NULL,
                team        TEXT,
                position    TEXT,
                ig_handle   TEXT UNIQUE NOT NULL,
                ig_user_id  TEXT,
                active      INTEGER NOT NULL DEFAULT 1,
                created_at  TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS following (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id       INTEGER NOT NULL REFERENCES players(id),
                ig_username     TEXT NOT NULL,
                ig_user_id      TEXT NOT NULL,
                ig_full_name    TEXT,
                ig_profile_pic  TEXT,
                first_seen      TEXT NOT NULL DEFAULT (datetime('now')),
                last_seen       TEXT NOT NULL DEFAULT (datetime('now')),
                is_current      INTEGER NOT NULL DEFAULT 1,
                UNIQUE(player_id, ig_user_id)
            );

            CREATE TABLE IF NOT EXISTS follow_events (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id       INTEGER NOT NULL REFERENCES players(id),
                event_type      TEXT NOT NULL CHECK(event_type IN ('follow','unfollow')),
                ig_username     TEXT NOT NULL,
                ig_user_id      TEXT NOT NULL,
                ig_full_name    TEXT,
                ig_profile_pic  TEXT,
                detected_at     TEXT NOT NULL DEFAULT (datetime('now')),
                posted_to_x     INTEGER NOT NULL DEFAULT 0,
                x_post_id       TEXT
            );

            CREATE INDEX IF NOT EXISTS idx_events_player
                ON follow_events(player_id, detected_at DESC);
            CREATE INDEX IF NOT EXISTS idx_events_detected
                ON follow_events(detected_at DESC);
            CREATE INDEX IF NOT EXISTS idx_following_player
                ON following(player_id, is_current);
        """)


# ---------------------------------------------------------------------------
# Players
# ---------------------------------------------------------------------------

def upsert_player(name, team, position, ig_handle, ig_user_id=None):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO players (name, team, position, ig_handle, ig_user_id)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(ig_handle) DO UPDATE SET
                name=excluded.name,
                team=excluded.team,
                position=excluded.position,
                ig_user_id=COALESCE(excluded.ig_user_id, ig_user_id)
        """, (name, team, position, ig_handle.lower().strip('@'), ig_user_id))


def get_all_players(active_only=True):
    with get_connection() as conn:
        q = "SELECT * FROM players"
        if active_only:
            q += " WHERE active=1"
        q += " ORDER BY name"
        return [dict(r) for r in conn.execute(q).fetchall()]


def get_player_by_id(player_id):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM players WHERE id=?", (player_id,)).fetchone()
        return dict(row) if row else None


def search_players(query):
    like = f"%{query}%"
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT * FROM players
            WHERE active=1 AND (name LIKE ? OR team LIKE ? OR ig_handle LIKE ?)
            ORDER BY name
        """, (like, like, like)).fetchall()
        return [dict(r) for r in rows]


def set_player_ig_user_id(player_id, ig_user_id):
    with get_connection() as conn:
        conn.execute("UPDATE players SET ig_user_id=? WHERE id=?", (ig_user_id, player_id))


# ---------------------------------------------------------------------------
# Following snapshot management
# ---------------------------------------------------------------------------

def get_current_following(player_id):
    """Return dict of {ig_user_id: row} for all current followings."""
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT * FROM following WHERE player_id=? AND is_current=1
        """, (player_id,)).fetchall()
        return {r['ig_user_id']: dict(r) for r in rows}


def update_following_snapshot(player_id, new_following: dict):
    """
    Diff the new following list against stored state.
    Returns (follows_added, follows_removed) as lists of dicts.
    new_following: {ig_user_id: {ig_username, ig_full_name, ig_profile_pic}}
    """
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    follows_added = []
    follows_removed = []

    with get_connection() as conn:
        existing = {
            r['ig_user_id']: dict(r)
            for r in conn.execute(
                "SELECT * FROM following WHERE player_id=? AND is_current=1",
                (player_id,)
            ).fetchall()
        }

        new_ids = set(new_following.keys())
        old_ids = set(existing.keys())

        # New follows
        for uid in new_ids - old_ids:
            data = new_following[uid]
            conn.execute("""
                INSERT INTO following
                    (player_id, ig_username, ig_user_id, ig_full_name, ig_profile_pic,
                     first_seen, last_seen, is_current)
                VALUES (?,?,?,?,?,?,?,1)
                ON CONFLICT(player_id, ig_user_id) DO UPDATE SET
                    last_seen=excluded.last_seen,
                    is_current=1,
                    ig_username=excluded.ig_username,
                    ig_full_name=excluded.ig_full_name,
                    ig_profile_pic=excluded.ig_profile_pic
            """, (player_id, data['ig_username'], uid,
                  data.get('ig_full_name'), data.get('ig_profile_pic'),
                  now, now))
            follows_added.append({'ig_user_id': uid, **data})

        # Unfollows
        for uid in old_ids - new_ids:
            data = existing[uid]
            conn.execute("""
                UPDATE following SET is_current=0, last_seen=?
                WHERE player_id=? AND ig_user_id=?
            """, (now, player_id, uid))
            follows_removed.append(data)

        # Update last_seen for unchanged
        for uid in old_ids & new_ids:
            conn.execute("""
                UPDATE following SET last_seen=? WHERE player_id=? AND ig_user_id=?
            """, (now, player_id, uid))

    return follows_added, follows_removed


# ---------------------------------------------------------------------------
# Follow events
# ---------------------------------------------------------------------------

def record_follow_event(player_id, event_type, ig_username, ig_user_id,
                         ig_full_name=None, ig_profile_pic=None):
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    with get_connection() as conn:
        cur = conn.execute("""
            INSERT INTO follow_events
                (player_id, event_type, ig_username, ig_user_id,
                 ig_full_name, ig_profile_pic, detected_at)
            VALUES (?,?,?,?,?,?,?)
        """, (player_id, event_type, ig_username, ig_user_id,
              ig_full_name, ig_profile_pic, now))
        return cur.lastrowid


def get_recent_events(limit=50, event_type=None, player_id=None):
    with get_connection() as conn:
        params = []
        where = []
        if event_type:
            where.append("e.event_type=?")
            params.append(event_type)
        if player_id:
            where.append("e.player_id=?")
            params.append(player_id)

        where_clause = ("WHERE " + " AND ".join(where)) if where else ""

        rows = conn.execute(f"""
            SELECT e.*, p.name as player_name, p.team, p.position,
                   p.ig_handle as player_ig_handle
            FROM follow_events e
            JOIN players p ON p.id = e.player_id
            {where_clause}
            ORDER BY e.detected_at DESC
            LIMIT ?
        """, params + [limit]).fetchall()
        return [dict(r) for r in rows]


def get_unposted_events(limit=20):
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT e.*, p.name as player_name, p.team, p.ig_handle as player_ig_handle
            FROM follow_events e
            JOIN players p ON p.id = e.player_id
            WHERE e.posted_to_x=0
            ORDER BY e.detected_at ASC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(r) for r in rows]


def mark_event_posted(event_id, x_post_id=None):
    with get_connection() as conn:
        conn.execute("""
            UPDATE follow_events SET posted_to_x=1, x_post_id=? WHERE id=?
        """, (x_post_id, event_id))


def count_x_posts_today():
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    with get_connection() as conn:
        row = conn.execute("""
            SELECT COUNT(*) as cnt FROM follow_events
            WHERE posted_to_x=1 AND detected_at LIKE ?
        """, (f"{today}%",)).fetchone()
        return row['cnt'] if row else 0


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def get_stats():
    with get_connection() as conn:
        stats = {}
        stats['total_players'] = conn.execute(
            "SELECT COUNT(*) FROM players WHERE active=1").fetchone()[0]
        stats['total_follows'] = conn.execute(
            "SELECT COUNT(*) FROM follow_events WHERE event_type='follow'").fetchone()[0]
        stats['total_unfollows'] = conn.execute(
            "SELECT COUNT(*) FROM follow_events WHERE event_type='unfollow'").fetchone()[0]
        stats['events_today'] = conn.execute(
            "SELECT COUNT(*) FROM follow_events WHERE detected_at LIKE ?",
            (datetime.now(timezone.utc).strftime('%Y-%m-%d') + '%',)
        ).fetchone()[0]
        return stats
