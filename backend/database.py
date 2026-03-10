"""
Database module — Supabase (PostgreSQL) backend.
All functions keep the same signatures as the original SQLite version
so tracker.py and x_poster.py need zero changes.
"""
import os
from datetime import datetime, timezone

from supabase import create_client, Client


def get_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if not url or not key:
        raise EnvironmentError(
            "SUPABASE_URL and SUPABASE_SERVICE_KEY must be set."
        )
    return create_client(url, key)


def init_db():
    """No-op for Supabase — tables are created via supabase_setup.sql."""
    pass


# ---------------------------------------------------------------------------
# Players
# ---------------------------------------------------------------------------

def upsert_player(name, team, position, ig_handle, ig_user_id=None):
    sb = get_client()
    sb.table('players').upsert(
        {
            'name': name,
            'team': team,
            'position': position,
            'ig_handle': ig_handle.lower().strip('@'),
            'ig_user_id': ig_user_id,
        },
        on_conflict='ig_handle',
    ).execute()


def get_all_players(active_only=True):
    sb = get_client()
    q = sb.table('players').select('*').order('name')
    if active_only:
        q = q.eq('active', True)
    return q.execute().data


def get_player_by_id(player_id):
    sb = get_client()
    result = sb.table('players').select('*').eq('id', player_id).execute()
    return result.data[0] if result.data else None


def search_players(query):
    sb = get_client()
    result = (
        sb.table('players')
        .select('*')
        .eq('active', True)
        .or_(f'name.ilike.%{query}%,team.ilike.%{query}%,ig_handle.ilike.%{query}%')
        .order('name')
        .execute()
    )
    return result.data


def set_player_ig_user_id(player_id, ig_user_id):
    sb = get_client()
    sb.table('players').update({'ig_user_id': ig_user_id}).eq('id', player_id).execute()


# ---------------------------------------------------------------------------
# Following snapshot
# ---------------------------------------------------------------------------

def get_current_following(player_id):
    sb = get_client()
    result = (
        sb.table('following')
        .select('*')
        .eq('player_id', player_id)
        .eq('is_current', True)
        .execute()
    )
    return {r['ig_user_id']: r for r in result.data}


def update_following_snapshot(player_id, new_following: dict):
    """
    Diff new following list against stored state.
    Returns (follows_added, follows_removed).
    """
    sb = get_client()
    now = datetime.now(timezone.utc).isoformat()

    existing = get_current_following(player_id)
    new_ids = set(new_following.keys())
    old_ids = set(existing.keys())

    follows_added = []
    follows_removed = []

    # New follows
    for uid in new_ids - old_ids:
        data = new_following[uid]
        sb.table('following').upsert(
            {
                'player_id': player_id,
                'ig_user_id': uid,
                'ig_username': data['ig_username'],
                'ig_full_name': data.get('ig_full_name'),
                'ig_profile_pic': data.get('ig_profile_pic'),
                'first_seen': now,
                'last_seen': now,
                'is_current': True,
            },
            on_conflict='player_id,ig_user_id',
        ).execute()
        follows_added.append({'ig_user_id': uid, **data})

    # Unfollows
    for uid in old_ids - new_ids:
        sb.table('following').update(
            {'is_current': False, 'last_seen': now}
        ).eq('player_id', player_id).eq('ig_user_id', uid).execute()
        follows_removed.append(existing[uid])

    # Refresh last_seen for unchanged accounts
    unchanged = list(old_ids & new_ids)
    if unchanged:
        sb.table('following').update({'last_seen': now}).eq(
            'player_id', player_id
        ).in_('ig_user_id', unchanged).execute()

    return follows_added, follows_removed


# ---------------------------------------------------------------------------
# Follow events
# ---------------------------------------------------------------------------

def record_follow_event(player_id, event_type, ig_username, ig_user_id,
                         ig_full_name=None, ig_profile_pic=None):
    sb = get_client()
    result = sb.table('follow_events').insert({
        'player_id': player_id,
        'event_type': event_type,
        'ig_username': ig_username,
        'ig_user_id': ig_user_id,
        'ig_full_name': ig_full_name,
        'ig_profile_pic': ig_profile_pic,
        'detected_at': datetime.now(timezone.utc).isoformat(),
        'posted_to_x': False,
    }).execute()
    return result.data[0]['id'] if result.data else None


def _flatten_events(rows):
    """Flatten Supabase nested join result into flat dicts."""
    events = []
    for ev in rows:
        player = ev.pop('players', None) or {}
        ev['player_name'] = player.get('name')
        ev['team'] = player.get('team')
        ev['position'] = player.get('position')
        ev['player_ig_handle'] = player.get('ig_handle')
        events.append(ev)
    return events


def get_recent_events(limit=50, event_type=None, player_id=None):
    sb = get_client()
    q = (
        sb.table('follow_events')
        .select('*, players(name, team, position, ig_handle)')
        .order('detected_at', desc=True)
        .limit(limit)
    )
    if event_type:
        q = q.eq('event_type', event_type)
    if player_id:
        q = q.eq('player_id', player_id)
    return _flatten_events(q.execute().data)


def get_unposted_events(limit=20):
    sb = get_client()
    result = (
        sb.table('follow_events')
        .select('*, players(name, team, ig_handle)')
        .eq('posted_to_x', False)
        .order('detected_at')
        .limit(limit)
        .execute()
    )
    return _flatten_events(result.data)


def mark_event_posted(event_id, x_post_id=None):
    sb = get_client()
    sb.table('follow_events').update(
        {'posted_to_x': True, 'x_post_id': x_post_id}
    ).eq('id', event_id).execute()


def count_x_posts_today():
    sb = get_client()
    today = datetime.now(timezone.utc).date().isoformat()
    result = (
        sb.table('follow_events')
        .select('id', count='exact')
        .eq('posted_to_x', True)
        .gte('detected_at', today)
        .execute()
    )
    return result.count or 0


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def get_stats():
    sb = get_client()
    today = datetime.now(timezone.utc).date().isoformat()

    p  = sb.table('players').select('id', count='exact').eq('active', True).execute()
    f  = sb.table('follow_events').select('id', count='exact').eq('event_type', 'follow').execute()
    u  = sb.table('follow_events').select('id', count='exact').eq('event_type', 'unfollow').execute()
    td = sb.table('follow_events').select('id', count='exact').gte('detected_at', today).execute()

    return {
        'total_players':   p.count  or 0,
        'total_follows':   f.count  or 0,
        'total_unfollows': u.count  or 0,
        'events_today':    td.count or 0,
    }
