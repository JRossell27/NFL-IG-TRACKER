-- ================================================================
-- NFL IG Tracker — Supabase Database Setup
--
-- HOW TO RUN:
--   1. Go to your Supabase project
--   2. Click "SQL Editor" in the left sidebar
--   3. Paste this entire file and click "Run"
-- ================================================================

-- Players tracked by the bot
CREATE TABLE IF NOT EXISTS players (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    team        TEXT,
    position    TEXT,
    ig_handle   TEXT UNIQUE NOT NULL,
    ig_user_id  TEXT,
    active      BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Current and historical following relationships
CREATE TABLE IF NOT EXISTS following (
    id              SERIAL PRIMARY KEY,
    player_id       INTEGER NOT NULL REFERENCES players(id),
    ig_username     TEXT NOT NULL,
    ig_user_id      TEXT NOT NULL,
    ig_full_name    TEXT,
    ig_profile_pic  TEXT,
    first_seen      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_seen       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    is_current      BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE(player_id, ig_user_id)
);

-- Every follow and unfollow event detected
CREATE TABLE IF NOT EXISTS follow_events (
    id              SERIAL PRIMARY KEY,
    player_id       INTEGER NOT NULL REFERENCES players(id),
    event_type      TEXT NOT NULL CHECK(event_type IN ('follow', 'unfollow')),
    ig_username     TEXT NOT NULL,
    ig_user_id      TEXT NOT NULL,
    ig_full_name    TEXT,
    ig_profile_pic  TEXT,
    detected_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    posted_to_x     BOOLEAN NOT NULL DEFAULT FALSE,
    x_post_id       TEXT
);

-- Indexes for fast queries
CREATE INDEX IF NOT EXISTS idx_events_player
    ON follow_events(player_id, detected_at DESC);
CREATE INDEX IF NOT EXISTS idx_events_detected
    ON follow_events(detected_at DESC);
CREATE INDEX IF NOT EXISTS idx_following_player
    ON following(player_id, is_current);

-- Allow read access for the anon/public role (Streamlit reads)
-- The service role key used by the tracker bypasses RLS
ALTER TABLE players       ENABLE ROW LEVEL SECURITY;
ALTER TABLE following     ENABLE ROW LEVEL SECURITY;
ALTER TABLE follow_events ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public read players"
    ON players FOR SELECT USING (TRUE);
CREATE POLICY "Public read following"
    ON following FOR SELECT USING (TRUE);
CREATE POLICY "Public read events"
    ON follow_events FOR SELECT USING (TRUE);
