"""
NFL players seed data with known Instagram handles.
Handles are best-effort accurate as of early 2025 — verify before use.
Run seed_players() once to populate the database.
"""

from backend.database import upsert_player

NFL_PLAYERS = [
    # ── Quarterbacks ──────────────────────────────────────────────────────
    {"name": "Patrick Mahomes",    "team": "Kansas City Chiefs",      "position": "QB", "ig_handle": "patrickmahomes"},
    {"name": "Josh Allen",         "team": "Buffalo Bills",            "position": "QB", "ig_handle": "joshallenqb"},
    {"name": "Lamar Jackson",      "team": "Baltimore Ravens",         "position": "QB", "ig_handle": "lj_era8"},
    {"name": "Jalen Hurts",        "team": "Philadelphia Eagles",      "position": "QB", "ig_handle": "jalenhurts"},
    {"name": "Joe Burrow",         "team": "Cincinnati Bengals",       "position": "QB", "ig_handle": "joeburrow9"},
    {"name": "Dak Prescott",       "team": "Dallas Cowboys",           "position": "QB", "ig_handle": "_dak"},
    {"name": "Justin Herbert",     "team": "Los Angeles Chargers",     "position": "QB", "ig_handle": "justinherbert"},
    {"name": "Tua Tagovailoa",     "team": "Miami Dolphins",           "position": "QB", "ig_handle": "tuatagovailoa"},
    {"name": "Brock Purdy",        "team": "San Francisco 49ers",      "position": "QB", "ig_handle": "brockpurdy13"},
    {"name": "Kyler Murray",       "team": "Arizona Cardinals",        "position": "QB", "ig_handle": "kyler1murray"},
    {"name": "Jordan Love",        "team": "Green Bay Packers",        "position": "QB", "ig_handle": "jordan3love"},
    {"name": "Trevor Lawrence",    "team": "Jacksonville Jaguars",     "position": "QB", "ig_handle": "tlawrence16"},
    {"name": "C.J. Stroud",        "team": "Houston Texans",           "position": "QB", "ig_handle": "cj.stroud7"},
    {"name": "Sam Darnold",        "team": "Minnesota Vikings",        "position": "QB", "ig_handle": "samdarnold14"},
    {"name": "Drake Maye",         "team": "New England Patriots",     "position": "QB", "ig_handle": "drakemaye10"},
    {"name": "Caleb Williams",     "team": "Chicago Bears",            "position": "QB", "ig_handle": "calebwilliams"},
    {"name": "Bo Nix",             "team": "Denver Broncos",           "position": "QB", "ig_handle": "bonix10"},

    # ── Wide Receivers ────────────────────────────────────────────────────
    {"name": "Tyreek Hill",        "team": "Miami Dolphins",           "position": "WR", "ig_handle": "cheetah"},
    {"name": "Justin Jefferson",   "team": "Minnesota Vikings",        "position": "WR", "ig_handle": "justinjefferson"},
    {"name": "CeeDee Lamb",        "team": "Dallas Cowboys",           "position": "WR", "ig_handle": "cdliii"},
    {"name": "Ja'Marr Chase",      "team": "Cincinnati Bengals",       "position": "WR", "ig_handle": "real10ja"},
    {"name": "Davante Adams",      "team": "New York Jets",            "position": "WR", "ig_handle": "tae15adams"},
    {"name": "Stefon Diggs",       "team": "New England Patriots",     "position": "WR", "ig_handle": "stefondiggs"},
    {"name": "DeAndre Hopkins",    "team": "Tennessee Titans",         "position": "WR", "ig_handle": "deandrehopkins"},
    {"name": "A.J. Brown",         "team": "Philadelphia Eagles",      "position": "WR", "ig_handle": "1randomkid_"},
    {"name": "Deebo Samuel",       "team": "San Francisco 49ers",      "position": "WR", "ig_handle": "debo"},
    {"name": "Cooper Kupp",        "team": "Los Angeles Rams",         "position": "WR", "ig_handle": "cooperkupp"},
    {"name": "Amon-Ra St. Brown",  "team": "Detroit Lions",            "position": "WR", "ig_handle": "amonrastbrown"},
    {"name": "Jaylen Waddle",      "team": "Miami Dolphins",           "position": "WR", "ig_handle": "jaywaddle17"},
    {"name": "DK Metcalf",         "team": "Seattle Seahawks",         "position": "WR", "ig_handle": "dkmetcalf14"},
    {"name": "Keenan Allen",       "team": "Chicago Bears",            "position": "WR", "ig_handle": "keenanallen13"},
    {"name": "Chris Olave",        "team": "New Orleans Saints",       "position": "WR", "ig_handle": "chrisolave_"},
    {"name": "Tee Higgins",        "team": "Cincinnati Bengals",       "position": "WR", "ig_handle": "teehiggins5"},
    {"name": "Puka Nacua",         "team": "Los Angeles Rams",         "position": "WR", "ig_handle": "pukanacua17"},
    {"name": "Rome Odunze",        "team": "Chicago Bears",            "position": "WR", "ig_handle": "romeodunze"},
    {"name": "Marvin Harrison Jr.","team": "Arizona Cardinals",        "position": "WR", "ig_handle": "marvharrisonjr"},

    # ── Tight Ends ────────────────────────────────────────────────────────
    {"name": "Travis Kelce",       "team": "Kansas City Chiefs",       "position": "TE", "ig_handle": "killatrav"},
    {"name": "Mark Andrews",       "team": "Baltimore Ravens",         "position": "TE", "ig_handle": "markandrews"},
    {"name": "George Kittle",      "team": "San Francisco 49ers",      "position": "TE", "ig_handle": "gkittle46"},
    {"name": "Sam LaPorta",        "team": "Detroit Lions",            "position": "TE", "ig_handle": "samla_porta"},
    {"name": "Dallas Goedert",     "team": "Philadelphia Eagles",      "position": "TE", "ig_handle": "dgoedert88"},
    {"name": "Evan Engram",        "team": "Jacksonville Jaguars",     "position": "TE", "ig_handle": "evan_engram"},
    {"name": "David Njoku",        "team": "Cleveland Browns",         "position": "TE", "ig_handle": "davidnjoku_"},

    # ── Running Backs ─────────────────────────────────────────────────────
    {"name": "Christian McCaffrey","team": "San Francisco 49ers",      "position": "RB", "ig_handle": "christianmccaffrey"},
    {"name": "Derrick Henry",      "team": "Baltimore Ravens",         "position": "RB", "ig_handle": "kinghenry_2"},
    {"name": "Saquon Barkley",     "team": "Philadelphia Eagles",      "position": "RB", "ig_handle": "saquon"},
    {"name": "Breece Hall",        "team": "New York Jets",            "position": "RB", "ig_handle": "breecehall20"},
    {"name": "Josh Jacobs",        "team": "Green Bay Packers",        "position": "RB", "ig_handle": "iamjoshjacobs"},
    {"name": "De'Von Achane",      "team": "Miami Dolphins",           "position": "RB", "ig_handle": "devon_achane6"},
    {"name": "Bijan Robinson",     "team": "Atlanta Falcons",          "position": "RB", "ig_handle": "bijan4robinson"},
    {"name": "Jahmyr Gibbs",       "team": "Detroit Lions",            "position": "RB", "ig_handle": "jahmyrgibbs"},
    {"name": "Tony Pollard",       "team": "Tennessee Titans",         "position": "RB", "ig_handle": "tonypollard"},
    {"name": "Aaron Jones",        "team": "Minnesota Vikings",        "position": "RB", "ig_handle": "showtyme33_aj"},

    # ── Defensive Players ─────────────────────────────────────────────────
    {"name": "Micah Parsons",      "team": "Dallas Cowboys",           "position": "LB", "ig_handle": "itsmicahparsons"},
    {"name": "Myles Garrett",      "team": "Cleveland Browns",         "position": "DE", "ig_handle": "flash_g2x"},
    {"name": "Nick Bosa",          "team": "San Francisco 49ers",      "position": "DE", "ig_handle": "nbsmallerbear"},
    {"name": "Maxx Crosby",        "team": "Las Vegas Raiders",        "position": "DE", "ig_handle": "maxxcrosby"},
    {"name": "T.J. Watt",          "team": "Pittsburgh Steelers",      "position": "LB", "ig_handle": "tj_watt"},
    {"name": "Sauce Gardner",      "team": "New York Jets",            "position": "CB", "ig_handle": "iamsauce_gardner"},
    {"name": "Jalen Ramsey",       "team": "Miami Dolphins",           "position": "CB", "ig_handle": "jalenramsey"},
    {"name": "Darius Slay",        "team": "Philadelphia Eagles",      "position": "CB", "ig_handle": "bigplay24slay"},
    {"name": "Roquan Smith",       "team": "Baltimore Ravens",         "position": "LB", "ig_handle": "roquan_smith0"},
    {"name": "Fred Warner",        "team": "San Francisco 49ers",      "position": "LB", "ig_handle": "fredwarner"},
    {"name": "Devin White",        "team": "Philadelphia Eagles",      "position": "LB", "ig_handle": "devinwhite__"},
    {"name": "Ja'Whaun Bentley",   "team": "New England Patriots",     "position": "LB", "ig_handle": "jawhaunbentley"},
    {"name": "Will Anderson Jr.",  "team": "Houston Texans",           "position": "DE", "ig_handle": "willandersonjr"},
    {"name": "Aidan Hutchinson",   "team": "Detroit Lions",            "position": "DE", "ig_handle": "aidanhutchinson"},
    {"name": "Haason Reddick",     "team": "New York Jets",            "position": "LB", "ig_handle": "haasonreddick7"},
    {"name": "Danielle Hunter",    "team": "Houston Texans",           "position": "DE", "ig_handle": "daniellehunter99"},

    # ── Offensive Line / Special ──────────────────────────────────────────
    {"name": "Lane Johnson",       "team": "Philadelphia Eagles",      "position": "OT", "ig_handle": "lanejohnson65"},
    {"name": "Trent Williams",     "team": "San Francisco 49ers",      "position": "OT", "ig_handle": "trent"},
]


def seed_players():
    """Populate the players table with the seed list. Safe to run multiple times."""
    for p in NFL_PLAYERS:
        upsert_player(
            name=p["name"],
            team=p["team"],
            position=p["position"],
            ig_handle=p["ig_handle"],
        )
    print(f"Seeded {len(NFL_PLAYERS)} NFL players.")


if __name__ == "__main__":
    from backend.database import init_db
    init_db()
    seed_players()
