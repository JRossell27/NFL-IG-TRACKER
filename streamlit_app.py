"""
NFL IG Tracker — Streamlit Web App
Companion website for the automated X bot.
"""
import os
import threading
import time
import requests as _requests
from datetime import datetime, timezone

import streamlit as st

# ── Bridge Streamlit secrets → os.environ (for backend modules) ──────────
for _k, _v in st.secrets.items():
    if isinstance(_v, str):
        os.environ.setdefault(_k, _v)

# ── Keep-alive ping (prevents Streamlit Cloud from sleeping) ──────────────
_ping_started = False

def _start_keep_alive():
    global _ping_started
    if _ping_started:
        return
    url = os.environ.get("STREAMLIT_APP_URL", "")
    if not url:
        return
    _ping_started = True

    def _ping():
        while True:
            time.sleep(300)  # ping every 5 minutes
            try:
                _requests.get(url, timeout=10)
            except Exception:
                pass

    t = threading.Thread(target=_ping, daemon=True)
    t.start()

_start_keep_alive()

from backend import database as db

# ── Page config ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NFL IG Tracker",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Dark background */
.stApp { background-color: #0b0f1a; color: #e2e8f0; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f1524;
    border-right: 1px solid #252d42;
}
section[data-testid="stSidebar"] .stMarkdown p { color: #94a3b8; font-size: 0.8rem; }

/* Inputs */
.stTextInput input {
    background-color: #141824 !important;
    border: 1px solid #252d42 !important;
    color: #e2e8f0 !important;
    border-radius: 8px !important;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: #141824;
    border: 1px solid #252d42;
    border-radius: 10px;
    padding: 12px 16px;
}
div[data-testid="metric-container"] label { color: #94a3b8 !important; font-size: 0.75rem !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
    color: #f59e0b !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
}

/* Radio buttons */
.stRadio label { color: #94a3b8 !important; font-size: 0.85rem !important; }
.stRadio div[role="radiogroup"] label[data-checked="true"] { color: #f59e0b !important; }

/* Selectbox */
.stSelectbox > div > div {
    background: #141824 !important;
    border-color: #252d42 !important;
    color: #e2e8f0 !important;
}

/* Remove default streamlit padding */
.block-container { padding-top: 1rem; }

/* Divider */
hr { border-color: #252d42; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0b0f1a; }
::-webkit-scrollbar-thumb { background: #252d42; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────

def relative_time(date_str: str) -> str:
    if not date_str:
        return "unknown"
    try:
        if date_str.endswith('Z'):
            date_str = date_str[:-1] + '+00:00'
        dt = datetime.fromisoformat(date_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        diff = (datetime.now(timezone.utc) - dt).total_seconds()
        if diff < 60:    return "just now"
        if diff < 3600:  return f"{int(diff/60)}m ago"
        if diff < 86400: return f"{int(diff/3600)}h ago"
        return f"{int(diff/86400)}d ago"
    except Exception:
        return date_str[:10]


def position_group(pos: str) -> str:
    p = (pos or '').upper()
    if p == 'QB': return 'QB'
    if p in ('WR',): return 'WR'
    if p in ('RB', 'FB'): return 'RB'
    if p == 'TE': return 'TE'
    if any(d in p for d in ('LB','DE','DT','CB','S','DB','EDGE')): return 'DEF'
    return 'other'


def event_card_html(ev: dict) -> str:
    is_follow = ev['event_type'] == 'follow'
    color  = '#10b981' if is_follow else '#ef4444'
    bg     = '#052e16' if is_follow else '#1a0404'
    verb   = 'followed' if is_follow else 'unfollowed'
    label  = '+ Follow' if is_follow else '− Unfollow'
    time_s = relative_time(ev.get('detected_at', ''))

    # Avatar
    pic = ev.get('ig_profile_pic', '')
    avatar = (
        f'<img src="{pic}" style="width:44px;height:44px;border-radius:50%;'
        f'object-fit:cover;border:2px solid #252d42" '
        f'onerror="this.style.display=\'none\'">'
        if pic else
        '<span style="font-size:1.5rem">👤</span>'
    )

    # Full name suffix
    full = ev.get('ig_full_name', '') or ''
    name_suffix = (
        f' <span style="color:#94a3b8;font-weight:400">({full})</span>'
        if full and full != ev.get('ig_username') else ''
    )

    # Player prefix (shown in "all players" view)
    player_prefix = ''
    if ev.get('player_name'):
        player_prefix = f'<strong style="color:#e2e8f0">{ev["player_name"]}</strong> '

    team_tag = (
        f'<span style="background:#1c2235;color:#94a3b8;padding:2px 6px;'
        f'border-radius:4px;font-size:0.68rem">{ev["team"]}</span>'
        if ev.get('team') else ''
    )

    return f"""
<div style="background:#141824;border:1px solid #252d42;border-left:3px solid {color};
            border-radius:10px;padding:14px 16px;margin-bottom:8px;
            display:flex;align-items:center;gap:14px">
  <div style="width:44px;height:44px;border-radius:50%;background:#1c2235;
              display:flex;align-items:center;justify-content:center;flex-shrink:0">
    {avatar}
  </div>
  <div style="flex:1;min-width:0">
    <div style="font-size:0.95rem;line-height:1.4">
      {player_prefix}<span style="color:{color};font-weight:500">{verb}</span>
      <strong style="color:#f59e0b"> @{ev.get('ig_username','')}</strong>{name_suffix}
      <span style="color:#94a3b8"> on Instagram</span>
    </div>
    <div style="font-size:0.75rem;color:#94a3b8;margin-top:5px;display:flex;gap:8px;flex-wrap:wrap;align-items:center">
      <span>{time_s}</span>
      <span style="background:{bg};color:{color};padding:2px 6px;border-radius:4px;font-size:0.68rem">{label}</span>
      {team_tag}
    </div>
  </div>
</div>
"""


# ── Session state defaults ────────────────────────────────────────────────
if 'selected_player_id' not in st.session_state:
    st.session_state.selected_player_id = None
if 'event_limit' not in st.session_state:
    st.session_state.event_limit = 50


# ── Load data ─────────────────────────────────────────────────────────────
@st.cache_data(ttl=60)
def load_players():
    return db.get_all_players()

@st.cache_data(ttl=60)
def load_stats():
    return db.get_stats()

@st.cache_data(ttl=60)
def load_events(player_id, event_type, limit):
    return db.get_recent_events(limit=limit, player_id=player_id, event_type=event_type)


# ── Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<h1 style="color:#f59e0b;font-size:1.3rem;margin-bottom:0">🏈 NFL IG Tracker</h1>',
        unsafe_allow_html=True,
    )
    st.caption("Real-time Instagram follow activity for NFL players")
    st.divider()

    search = st.text_input("Search players or teams", placeholder="e.g. Mahomes, Chiefs…")
    pos_filter = st.selectbox(
        "Filter by position",
        ["All", "QB", "WR", "RB", "TE", "DEF"],
    )

    st.divider()

    players = load_players()

    # Apply filters
    filtered = [
        p for p in players
        if (not search or
            search.lower() in p['name'].lower() or
            search.lower() in (p.get('team') or '').lower() or
            search.lower() in (p.get('ig_handle') or '').lower())
        and (pos_filter == 'All' or position_group(p.get('position', '')) == pos_filter
             or p.get('position', '').upper() == pos_filter)
    ]

    st.markdown(
        f'<p style="color:#64748b;font-size:0.75rem;margin-bottom:8px">'
        f'{len(filtered)} player{"s" if len(filtered) != 1 else ""}</p>',
        unsafe_allow_html=True,
    )

    # "All players" button
    if st.button(
        "📋 All Players",
        use_container_width=True,
        type="primary" if st.session_state.selected_player_id is None else "secondary",
    ):
        st.session_state.selected_player_id = None
        st.session_state.event_limit = 50
        st.cache_data.clear()

    for p in filtered:
        is_active = st.session_state.selected_player_id == p['id']
        label = f"{'▶ ' if is_active else ''}{p['name']}"
        if st.button(
            label,
            key=f"p_{p['id']}",
            use_container_width=True,
            help=f"@{p['ig_handle']} · {p.get('team','')} · {p.get('position','')}",
        ):
            st.session_state.selected_player_id = p['id']
            st.session_state.event_limit = 50
            st.cache_data.clear()

    st.divider()
    st.caption("Data refreshes every 4 hours via GitHub Actions.\nFollow us on X @NFLIGTracker")


# ── Main content ──────────────────────────────────────────────────────────

# Stats row
stats = load_stats()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Players Tracked", stats['total_players'])
c2.metric("Total Follows",   f"{stats['total_follows']:,}")
c3.metric("Total Unfollows", f"{stats['total_unfollows']:,}")
c4.metric("Activity Today",  stats['events_today'])

st.divider()

# Title + filter controls
selected_id = st.session_state.selected_player_id
selected_player = next((p for p in players if p['id'] == selected_id), None) if selected_id else None

col_title, col_filter = st.columns([3, 2])

with col_title:
    if selected_player:
        st.markdown(
            f'<h2 style="color:#e2e8f0;margin:0">{selected_player["name"]}</h2>'
            f'<p style="color:#94a3b8;margin:0;font-size:0.85rem">'
            f'@{selected_player["ig_handle"]} &nbsp;·&nbsp; {selected_player.get("team","")}'
            f' &nbsp;·&nbsp; {selected_player.get("position","")}</p>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<h2 style="color:#e2e8f0;margin:0">Recent Activity</h2>'
            '<p style="color:#94a3b8;margin:0;font-size:0.85rem">All players · latest follows &amp; unfollows</p>',
            unsafe_allow_html=True,
        )

with col_filter:
    ev_type_label = st.radio(
        "Show",
        ["All", "Follows", "Unfollows"],
        horizontal=True,
        label_visibility="collapsed",
    )

ev_type_param = {"All": None, "Follows": "follow", "Unfollows": "unfollow"}[ev_type_label]

# ── Event feed ────────────────────────────────────────────────────────────
events = load_events(selected_id, ev_type_param, st.session_state.event_limit)

if not events:
    st.markdown(
        '<div style="text-align:center;padding:60px 20px;color:#64748b">'
        '<div style="font-size:2.5rem;margin-bottom:12px">📭</div>'
        '<p>No activity recorded yet.<br>Check back after the next tracking run.</p>'
        '</div>',
        unsafe_allow_html=True,
    )
else:
    for ev in events:
        st.markdown(event_card_html(ev), unsafe_allow_html=True)

    if len(events) >= st.session_state.event_limit:
        if st.button("Load more", use_container_width=False):
            st.session_state.event_limit += 50
            st.cache_data.clear()
            st.rerun()

# ── Auto-refresh every 60 seconds ────────────────────────────────────────
st.markdown(
    '<meta http-equiv="refresh" content="60">',
    unsafe_allow_html=True,
)
