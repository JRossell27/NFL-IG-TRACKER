/* =========================================================
   NFL IG Tracker — Frontend App
   Vanilla JS SPA that talks to the Flask REST API
   ========================================================= */

const API_BASE = window.location.origin + '/api';

// ── State ──────────────────────────────────────────────────
const state = {
  players: [],
  filteredPlayers: [],
  selectedPlayer: null,
  eventType: 'all',       // 'all' | 'follow' | 'unfollow'
  posFilter: 'all',
  searchQuery: '',
  events: [],
  eventsLimit: 50,
  eventsPage: 1,
};

// ── DOM refs ───────────────────────────────────────────────
const $playerList    = document.getElementById('playerList');
const $playerSearch  = document.getElementById('playerSearch');
const $feed          = document.getElementById('feed');
const $feedTitle     = document.getElementById('feedTitle').querySelector('span');
const $feedSubtitle  = document.getElementById('feedSubtitle');
const $backBtn       = document.getElementById('backBtn');
const $loadMore      = document.getElementById('loadMore');
const $loadMoreBtn   = document.getElementById('loadMoreBtn');
const $modal         = document.getElementById('playerModal');
const $modalContent  = document.getElementById('modalContent');
const $modalClose    = document.getElementById('modalClose');
const $modalBackdrop = document.getElementById('modalBackdrop');
const $statPlayers   = document.getElementById('statPlayers');
const $statFollows   = document.getElementById('statFollows');
const $statUnfollows = document.getElementById('statUnfollows');

// ── Utility ────────────────────────────────────────────────

async function apiFetch(path) {
  const res = await fetch(API_BASE + path);
  if (!res.ok) throw new Error(`API error ${res.status}: ${path}`);
  return res.json();
}

function relativeTime(dateStr) {
  const date = new Date(dateStr + (dateStr.endsWith('Z') ? '' : 'Z'));
  const diff = (Date.now() - date.getTime()) / 1000;
  if (diff < 60)   return 'just now';
  if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}h ago`;
  if (diff < 604800) return `${Math.floor(diff / 86400)}d ago`;
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

function playerInitials(name) {
  return name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
}

function positionGroup(pos) {
  if (!pos) return 'other';
  const p = pos.toUpperCase();
  if (['QB'].includes(p))                    return 'QB';
  if (['WR', 'TE', 'K'].includes(p))         return 'WR';
  if (['RB', 'FB'].includes(p))              return 'RB';
  if (['TE'].includes(p))                    return 'TE';
  if (['LB','DE','DT','CB','S','DB','EDGE'].some(d => p.includes(d))) return 'DEF';
  return 'other';
}

// ── Stats ──────────────────────────────────────────────────

async function loadStats() {
  try {
    const s = await apiFetch('/stats');
    $statPlayers.textContent   = s.total_players;
    $statFollows.textContent   = s.total_follows.toLocaleString();
    $statUnfollows.textContent = s.total_unfollows.toLocaleString();
  } catch (e) {
    console.warn('Stats load failed:', e);
  }
}

// ── Players ────────────────────────────────────────────────

async function loadPlayers() {
  try {
    state.players = await apiFetch('/players');
    applyFilters();
  } catch (e) {
    $playerList.innerHTML = '<div class="empty-state"><p>Could not load players.</p></div>';
  }
}

function applyFilters() {
  const q   = state.searchQuery.toLowerCase();
  const pos = state.posFilter;

  state.filteredPlayers = state.players.filter(p => {
    const matchSearch = !q ||
      p.name.toLowerCase().includes(q) ||
      (p.team || '').toLowerCase().includes(q) ||
      (p.ig_handle || '').toLowerCase().includes(q);
    const matchPos = pos === 'all' || positionGroup(p.position) === pos || p.position === pos;
    return matchSearch && matchPos;
  });

  renderPlayerList();
}

function renderPlayerList() {
  if (!state.filteredPlayers.length) {
    $playerList.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">🔍</div>
        <p>No players found</p>
      </div>`;
    return;
  }

  $playerList.innerHTML = state.filteredPlayers.map(p => `
    <div
      class="player-card ${state.selectedPlayer?.id === p.id ? 'active' : ''}"
      data-id="${p.id}"
      role="button"
      tabindex="0"
      aria-label="${p.name}"
    >
      <div class="player-avatar">${playerInitials(p.name)}</div>
      <div class="player-info">
        <div class="player-name">${escHtml(p.name)}</div>
        <div class="player-meta">${escHtml(p.team || '')} &middot; @${escHtml(p.ig_handle)}</div>
      </div>
      <span class="player-badge">${escHtml(p.position || '—')}</span>
    </div>
  `).join('');

  // Attach click handlers
  $playerList.querySelectorAll('.player-card').forEach(card => {
    card.addEventListener('click', () => selectPlayer(parseInt(card.dataset.id)));
    card.addEventListener('keypress', e => {
      if (e.key === 'Enter') selectPlayer(parseInt(card.dataset.id));
    });
  });
}

// ── Select Player ──────────────────────────────────────────

function selectPlayer(id) {
  const player = state.players.find(p => p.id === id);
  if (!player) return;
  state.selectedPlayer = player;
  state.eventsPage = 1;
  state.eventsLimit = 50;

  renderPlayerList();
  $feedTitle.textContent = player.name;
  $feedSubtitle.textContent = `@${player.ig_handle} · ${player.team || ''}`;
  $backBtn.classList.remove('hidden');

  loadPlayerEvents();
}

function clearSelection() {
  state.selectedPlayer = null;
  state.eventsPage = 1;
  state.eventsLimit = 50;
  renderPlayerList();
  $feedTitle.textContent = 'Recent Activity';
  $feedSubtitle.textContent = 'All players · latest follows & unfollows';
  $backBtn.classList.add('hidden');
  loadRecentEvents();
}

// ── Events ─────────────────────────────────────────────────

async function loadRecentEvents() {
  $feed.innerHTML = '<div class="loading-spinner">Loading activity…</div>';
  $loadMore.classList.add('hidden');
  try {
    const typeParam = state.eventType !== 'all' ? `&type=${state.eventType}` : '';
    const events = await apiFetch(`/events/recent?limit=${state.eventsLimit}${typeParam}`);
    state.events = events;
    renderFeed();
  } catch (e) {
    $feed.innerHTML = '<div class="empty-state"><p>Could not load events.</p></div>';
  }
}

async function loadPlayerEvents() {
  $feed.innerHTML = '<div class="loading-spinner">Loading activity…</div>';
  $loadMore.classList.add('hidden');
  try {
    const typeParam = state.eventType !== 'all' ? `&type=${state.eventType}` : '';
    const data = await apiFetch(
      `/players/${state.selectedPlayer.id}/events?limit=${state.eventsLimit}${typeParam}`
    );
    state.events = data.events;
    renderFeed();
  } catch (e) {
    $feed.innerHTML = '<div class="empty-state"><p>Could not load events.</p></div>';
  }
}

function renderFeed() {
  if (!state.events.length) {
    $feed.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">📭</div>
        <p>No activity recorded yet.<br>Check back after the next tracking run.</p>
      </div>`;
    $loadMore.classList.add('hidden');
    return;
  }

  $feed.innerHTML = state.events.map(ev => renderEventCard(ev)).join('');

  // Show load more if we got a full page
  if (state.events.length >= state.eventsLimit) {
    $loadMore.classList.remove('hidden');
  } else {
    $loadMore.classList.add('hidden');
  }
}

function renderEventCard(ev) {
  const isFollow = ev.event_type === 'follow';
  const verbText = isFollow ? 'followed' : 'unfollowed';
  const avatarHtml = ev.ig_profile_pic
    ? `<img src="${escHtml(ev.ig_profile_pic)}" alt="${escHtml(ev.ig_username)}" loading="lazy" onerror="this.style.display='none';this.parentElement.textContent='👤'">`
    : '👤';

  const playerLine = ev.player_name
    ? `<span class="event-player">${escHtml(ev.player_name)}</span> `
    : '';

  const fullName = ev.ig_full_name && ev.ig_full_name !== ev.ig_username
    ? ` <span style="color:var(--text-muted);font-weight:400">(${escHtml(ev.ig_full_name)})</span>`
    : '';

  return `
    <div class="event-card ${ev.event_type}">
      <div class="event-avatar">${avatarHtml}</div>
      <div class="event-body">
        <div class="event-main">
          ${playerLine}<span class="event-verb ${ev.event_type}">${verbText}</span>
          <span class="event-target"> @${escHtml(ev.ig_username)}</span>${fullName}
          <span style="color:var(--text-muted)"> on Instagram</span>
        </div>
        <div class="event-meta">
          <span class="event-time">${relativeTime(ev.detected_at)}</span>
          <span class="event-tag ${ev.event_type}">${isFollow ? '+ Follow' : '− Unfollow'}</span>
          ${ev.team ? `<span class="event-tag">${escHtml(ev.team)}</span>` : ''}
        </div>
      </div>
      <div class="event-side">
        ${new Date(ev.detected_at + (ev.detected_at.endsWith('Z') ? '' : 'Z'))
          .toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
      </div>
    </div>
  `;
}

function escHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Event type toggle ─────────────────────────────────────

document.querySelectorAll('.type-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.type-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    state.eventType = btn.dataset.type;
    state.eventsLimit = 50;
    if (state.selectedPlayer) {
      loadPlayerEvents();
    } else {
      loadRecentEvents();
    }
  });
});

// ── Position filter ───────────────────────────────────────

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    state.posFilter = btn.dataset.filter;
    applyFilters();
  });
});

// ── Search ─────────────────────────────────────────────────

let searchDebounce;
$playerSearch.addEventListener('input', () => {
  clearTimeout(searchDebounce);
  searchDebounce = setTimeout(() => {
    state.searchQuery = $playerSearch.value.trim();
    applyFilters();
  }, 200);
});

// ── Back button ────────────────────────────────────────────

$backBtn.addEventListener('click', clearSelection);

// ── Load more ──────────────────────────────────────────────

$loadMoreBtn.addEventListener('click', () => {
  state.eventsLimit += 50;
  if (state.selectedPlayer) {
    loadPlayerEvents();
  } else {
    loadRecentEvents();
  }
});

// ── Modal (future use for player detail popup) ─────────────

$modalClose.addEventListener('click', closeModal);
$modalBackdrop.addEventListener('click', closeModal);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });

function closeModal() { $modal.classList.add('hidden'); }

// ── Auto-refresh every 5 minutes ──────────────────────────

setInterval(() => {
  loadStats();
  if (state.selectedPlayer) {
    loadPlayerEvents();
  } else {
    loadRecentEvents();
  }
}, 5 * 60 * 1000);

// ── Init ───────────────────────────────────────────────────

(async function init() {
  await Promise.all([loadStats(), loadPlayers(), loadRecentEvents()]);
})();
