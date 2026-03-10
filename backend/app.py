"""
Flask REST API — serves both the JSON API and the static frontend.
"""
import os
import logging
from flask import Flask, jsonify, request, send_from_directory, abort
from flask_cors import CORS

from backend import database as db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')
CORS(app)


# ---------------------------------------------------------------------------
# Frontend
# ---------------------------------------------------------------------------

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path and os.path.exists(os.path.join(FRONTEND_DIR, path)):
        return send_from_directory(FRONTEND_DIR, path)
    return send_from_directory(FRONTEND_DIR, 'index.html')


# ---------------------------------------------------------------------------
# Players
# ---------------------------------------------------------------------------

@app.get('/api/players')
def api_players():
    q = request.args.get('search', '').strip()
    if q:
        players = db.search_players(q)
    else:
        players = db.get_all_players()

    # Enrich with event counts
    return jsonify(players)


@app.get('/api/players/<int:player_id>')
def api_player_detail(player_id):
    player = db.get_player_by_id(player_id)
    if not player:
        abort(404, description="Player not found")
    return jsonify(player)


@app.get('/api/players/<int:player_id>/events')
def api_player_events(player_id):
    player = db.get_player_by_id(player_id)
    if not player:
        abort(404, description="Player not found")

    limit = min(int(request.args.get('limit', 50)), 200)
    event_type = request.args.get('type')  # 'follow' | 'unfollow' | None
    events = db.get_recent_events(limit=limit, event_type=event_type, player_id=player_id)
    return jsonify({"player": player, "events": events})


@app.get('/api/players/<int:player_id>/following')
def api_player_following(player_id):
    player = db.get_player_by_id(player_id)
    if not player:
        abort(404, description="Player not found")
    following = db.get_current_following(player_id)
    return jsonify({
        "player": player,
        "following": list(following.values()),
        "count": len(following),
    })


# ---------------------------------------------------------------------------
# Events
# ---------------------------------------------------------------------------

@app.get('/api/events/recent')
def api_recent_events():
    limit = min(int(request.args.get('limit', 50)), 200)
    event_type = request.args.get('type')
    events = db.get_recent_events(limit=limit, event_type=event_type)
    return jsonify(events)


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

@app.get('/api/stats')
def api_stats():
    return jsonify(db.get_stats())


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e)}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def create_app():
    db.init_db()
    return app


if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    create_app().run(host='0.0.0.0', port=port, debug=debug)
