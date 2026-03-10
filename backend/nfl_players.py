"""
NFL players seed data — best-effort Instagram handles as of early 2025.
The tracker logs a warning and skips any handle that doesn't resolve;
it's safe to re-run seed_players() after adding/correcting entries.
"""

from backend.database import upsert_player

NFL_PLAYERS = [

    # ════════════════════════════════════════════════════════════════════════
    # AFC EAST
    # ════════════════════════════════════════════════════════════════════════

    # ── Buffalo Bills ─────────────────────────────────────────────────────
    {"name": "Josh Allen",           "team": "Buffalo Bills",           "position": "QB",  "ig_handle": "joshallenqb"},
    {"name": "Keon Coleman",         "team": "Buffalo Bills",           "position": "WR",  "ig_handle": "keoncoleman22"},
    {"name": "Khalil Shakir",        "team": "Buffalo Bills",           "position": "WR",  "ig_handle": "khalilshakir"},
    {"name": "James Cook",           "team": "Buffalo Bills",           "position": "RB",  "ig_handle": "jamescook"},
    {"name": "Dalton Kincaid",       "team": "Buffalo Bills",           "position": "TE",  "ig_handle": "daltonkincaid86"},
    {"name": "Von Miller",           "team": "Buffalo Bills",           "position": "LB",  "ig_handle": "vonmiller"},
    {"name": "Ed Oliver",            "team": "Buffalo Bills",           "position": "DT",  "ig_handle": "edoliver91"},
    {"name": "Taron Johnson",        "team": "Buffalo Bills",           "position": "CB",  "ig_handle": "taronj22"},
    {"name": "Tre'Davious White",    "team": "Buffalo Bills",           "position": "CB",  "ig_handle": "tredaviouswhite"},

    # ── Miami Dolphins ────────────────────────────────────────────────────
    {"name": "Tua Tagovailoa",       "team": "Miami Dolphins",          "position": "QB",  "ig_handle": "tuatagovailoa"},
    {"name": "Tyreek Hill",          "team": "Miami Dolphins",          "position": "WR",  "ig_handle": "cheetah"},
    {"name": "Jaylen Waddle",        "team": "Miami Dolphins",          "position": "WR",  "ig_handle": "jaywaddle17"},
    {"name": "De'Von Achane",        "team": "Miami Dolphins",          "position": "RB",  "ig_handle": "devon_achane6"},
    {"name": "Jonnu Smith",          "team": "Miami Dolphins",          "position": "TE",  "ig_handle": "jonnusmith"},
    {"name": "Jalen Ramsey",         "team": "Miami Dolphins",          "position": "CB",  "ig_handle": "jalenramsey"},
    {"name": "Jevon Holland",        "team": "Miami Dolphins",          "position": "S",   "ig_handle": "jevonholland"},
    {"name": "Bradley Chubb",        "team": "Miami Dolphins",          "position": "LB",  "ig_handle": "bradleychubb2"},
    {"name": "Christian Wilkins",    "team": "Miami Dolphins",          "position": "DT",  "ig_handle": "christianwilkins97"},

    # ── New England Patriots ──────────────────────────────────────────────
    {"name": "Drake Maye",           "team": "New England Patriots",    "position": "QB",  "ig_handle": "drakemaye10"},
    {"name": "Stefon Diggs",         "team": "New England Patriots",    "position": "WR",  "ig_handle": "stefondiggs"},
    {"name": "JuJu Smith-Schuster",  "team": "New England Patriots",    "position": "WR",  "ig_handle": "juju"},
    {"name": "Rhamondre Stevenson",  "team": "New England Patriots",    "position": "RB",  "ig_handle": "rhamondre21"},
    {"name": "Hunter Henry",         "team": "New England Patriots",    "position": "TE",  "ig_handle": "hunterhenry89"},
    {"name": "Christian Barmore",    "team": "New England Patriots",    "position": "DT",  "ig_handle": "christianbarmore"},
    {"name": "Ja'Whaun Bentley",     "team": "New England Patriots",    "position": "LB",  "ig_handle": "jawhaunbentley"},

    # ── New York Jets ─────────────────────────────────────────────────────
    {"name": "Aaron Rodgers",        "team": "New York Jets",           "position": "QB",  "ig_handle": "aaronrodgers12"},
    {"name": "Garrett Wilson",       "team": "New York Jets",           "position": "WR",  "ig_handle": "garrettwilson5"},
    {"name": "Davante Adams",        "team": "New York Jets",           "position": "WR",  "ig_handle": "tae15adams"},
    {"name": "Breece Hall",          "team": "New York Jets",           "position": "RB",  "ig_handle": "breecehall20"},
    {"name": "Tyler Conklin",        "team": "New York Jets",           "position": "TE",  "ig_handle": "tylerconklin83"},
    {"name": "Sauce Gardner",        "team": "New York Jets",           "position": "CB",  "ig_handle": "iamsauce_gardner"},
    {"name": "Haason Reddick",       "team": "New York Jets",           "position": "LB",  "ig_handle": "haasonreddick7"},
    {"name": "Quinnen Williams",     "team": "New York Jets",           "position": "DT",  "ig_handle": "quinnenwilliams95"},

    # ════════════════════════════════════════════════════════════════════════
    # AFC NORTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Baltimore Ravens ──────────────────────────────────────────────────
    {"name": "Lamar Jackson",        "team": "Baltimore Ravens",        "position": "QB",  "ig_handle": "lj_era8"},
    {"name": "Derrick Henry",        "team": "Baltimore Ravens",        "position": "RB",  "ig_handle": "kinghenry_2"},
    {"name": "Mark Andrews",         "team": "Baltimore Ravens",        "position": "TE",  "ig_handle": "markandrews"},
    {"name": "Zay Flowers",          "team": "Baltimore Ravens",        "position": "WR",  "ig_handle": "zayflowers4"},
    {"name": "Nelson Agholor",       "team": "Baltimore Ravens",        "position": "WR",  "ig_handle": "nelsonagholor"},
    {"name": "Roquan Smith",         "team": "Baltimore Ravens",        "position": "LB",  "ig_handle": "roquan_smith0"},
    {"name": "Kyle Hamilton",        "team": "Baltimore Ravens",        "position": "S",   "ig_handle": "kylehamilton"},
    {"name": "Marlon Humphrey",      "team": "Baltimore Ravens",        "position": "CB",  "ig_handle": "marlonhumphrey"},
    {"name": "Justin Madubuike",     "team": "Baltimore Ravens",        "position": "DT",  "ig_handle": "justinmadubuike"},

    # ── Cincinnati Bengals ────────────────────────────────────────────────
    {"name": "Joe Burrow",           "team": "Cincinnati Bengals",      "position": "QB",  "ig_handle": "joeburrow9"},
    {"name": "Ja'Marr Chase",        "team": "Cincinnati Bengals",      "position": "WR",  "ig_handle": "real10ja"},
    {"name": "Tee Higgins",          "team": "Cincinnati Bengals",      "position": "WR",  "ig_handle": "teehiggins5"},
    {"name": "Tyler Boyd",           "team": "Cincinnati Bengals",      "position": "WR",  "ig_handle": "tylerboyd83"},
    {"name": "Drew Sample",          "team": "Cincinnati Bengals",      "position": "TE",  "ig_handle": "drewsample"},
    {"name": "Zack Moss",            "team": "Cincinnati Bengals",      "position": "RB",  "ig_handle": "zackmoss"},
    {"name": "Trey Hendrickson",     "team": "Cincinnati Bengals",      "position": "DE",  "ig_handle": "treyhendrickson"},
    {"name": "Germaine Pratt",       "team": "Cincinnati Bengals",      "position": "LB",  "ig_handle": "germaine_pratt"},
    {"name": "Cam Taylor-Britt",     "team": "Cincinnati Bengals",      "position": "CB",  "ig_handle": "camtaylorbritt"},

    # ── Cleveland Browns ──────────────────────────────────────────────────
    {"name": "Deshaun Watson",       "team": "Cleveland Browns",        "position": "QB",  "ig_handle": "deshaunwatson"},
    {"name": "Amari Cooper",         "team": "Cleveland Browns",        "position": "WR",  "ig_handle": "amaricooper9"},
    {"name": "Jerry Jeudy",          "team": "Cleveland Browns",        "position": "WR",  "ig_handle": "jerryjeudy"},
    {"name": "David Njoku",          "team": "Cleveland Browns",        "position": "TE",  "ig_handle": "davidnjoku_"},
    {"name": "Nick Chubb",           "team": "Cleveland Browns",        "position": "RB",  "ig_handle": "nickchubb21"},
    {"name": "Jerome Ford",          "team": "Cleveland Browns",        "position": "RB",  "ig_handle": "jeromeford"},
    {"name": "Myles Garrett",        "team": "Cleveland Browns",        "position": "DE",  "ig_handle": "flash_g2x"},
    {"name": "Denzel Ward",          "team": "Cleveland Browns",        "position": "CB",  "ig_handle": "denzelward21"},
    {"name": "Juan Thornhill",       "team": "Cleveland Browns",        "position": "S",   "ig_handle": "juanthornhill22"},

    # ── Pittsburgh Steelers ───────────────────────────────────────────────
    {"name": "Justin Fields",        "team": "Pittsburgh Steelers",     "position": "QB",  "ig_handle": "justnfields1"},
    {"name": "George Pickens",       "team": "Pittsburgh Steelers",     "position": "WR",  "ig_handle": "gee_pickens"},
    {"name": "Pat Freiermuth",       "team": "Pittsburgh Steelers",     "position": "TE",  "ig_handle": "patfreiermuth"},
    {"name": "Najee Harris",         "team": "Pittsburgh Steelers",     "position": "RB",  "ig_handle": "najeeharris22"},
    {"name": "T.J. Watt",            "team": "Pittsburgh Steelers",     "position": "LB",  "ig_handle": "tj_watt"},
    {"name": "Minkah Fitzpatrick",   "team": "Pittsburgh Steelers",     "position": "S",   "ig_handle": "minkah"},
    {"name": "Cameron Heyward",      "team": "Pittsburgh Steelers",     "position": "DT",  "ig_handle": "camhey"},
    {"name": "Patrick Queen",        "team": "Pittsburgh Steelers",     "position": "LB",  "ig_handle": "patqueen6"},
    {"name": "Joey Porter Jr.",      "team": "Pittsburgh Steelers",     "position": "CB",  "ig_handle": "joeyporterjr"},

    # ════════════════════════════════════════════════════════════════════════
    # AFC SOUTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Houston Texans ────────────────────────────────────────────────────
    {"name": "C.J. Stroud",          "team": "Houston Texans",          "position": "QB",  "ig_handle": "cj.stroud7"},
    {"name": "Nico Collins",         "team": "Houston Texans",          "position": "WR",  "ig_handle": "nicocollins4"},
    {"name": "Tank Dell",            "team": "Houston Texans",          "position": "WR",  "ig_handle": "tankdell3"},
    {"name": "Dalton Schultz",       "team": "Houston Texans",          "position": "TE",  "ig_handle": "dalton.schultz86"},
    {"name": "Joe Mixon",            "team": "Houston Texans",          "position": "RB",  "ig_handle": "joemixon21"},
    {"name": "Will Anderson Jr.",    "team": "Houston Texans",          "position": "DE",  "ig_handle": "willandersonjr"},
    {"name": "Danielle Hunter",      "team": "Houston Texans",          "position": "DE",  "ig_handle": "daniellehunter99"},
    {"name": "Derek Stingley Jr.",   "team": "Houston Texans",          "position": "CB",  "ig_handle": "derek_stingley2"},
    {"name": "Jalen Pitre",          "team": "Houston Texans",          "position": "S",   "ig_handle": "jalenpitre"},

    # ── Indianapolis Colts ────────────────────────────────────────────────
    {"name": "Anthony Richardson",  "team": "Indianapolis Colts",      "position": "QB",  "ig_handle": "antr_5"},
    {"name": "Michael Pittman Jr.", "team": "Indianapolis Colts",      "position": "WR",  "ig_handle": "mpittmanjr"},
    {"name": "Josh Downs",           "team": "Indianapolis Colts",      "position": "WR",  "ig_handle": "joshuadowns9"},
    {"name": "Mo Alie-Cox",          "team": "Indianapolis Colts",      "position": "TE",  "ig_handle": "moaliecox"},
    {"name": "Jonathan Taylor",      "team": "Indianapolis Colts",      "position": "RB",  "ig_handle": "jontaylor"},
    {"name": "DeForest Buckner",     "team": "Indianapolis Colts",      "position": "DT",  "ig_handle": "deforest_buckner"},
    {"name": "Kwity Paye",           "team": "Indianapolis Colts",      "position": "DE",  "ig_handle": "kwitypaye"},
    {"name": "E.J. Speed",           "team": "Indianapolis Colts",      "position": "LB",  "ig_handle": "ejspeed54"},
    {"name": "Kenny Moore II",       "team": "Indianapolis Colts",      "position": "CB",  "ig_handle": "kennymoore_2"},

    # ── Jacksonville Jaguars ──────────────────────────────────────────────
    {"name": "Trevor Lawrence",      "team": "Jacksonville Jaguars",    "position": "QB",  "ig_handle": "tlawrence16"},
    {"name": "Brian Thomas Jr.",     "team": "Jacksonville Jaguars",    "position": "WR",  "ig_handle": "brianthomaspwr"},
    {"name": "Christian Kirk",       "team": "Jacksonville Jaguars",    "position": "WR",  "ig_handle": "christiankirk"},
    {"name": "Evan Engram",          "team": "Jacksonville Jaguars",    "position": "TE",  "ig_handle": "evan_engram"},
    {"name": "Travis Etienne",       "team": "Jacksonville Jaguars",    "position": "RB",  "ig_handle": "travisetienne"},
    {"name": "Josh Allen",           "team": "Jacksonville Jaguars",    "position": "LB",  "ig_handle": "joshallen41_"},
    {"name": "Tyson Campbell",       "team": "Jacksonville Jaguars",    "position": "CB",  "ig_handle": "tysoncampbell"},
    {"name": "Andre Cisco",          "team": "Jacksonville Jaguars",    "position": "S",   "ig_handle": "andrecisco"},

    # ── Tennessee Titans ──────────────────────────────────────────────────
    {"name": "Will Levis",           "team": "Tennessee Titans",        "position": "QB",  "ig_handle": "willlevis"},
    {"name": "DeAndre Hopkins",      "team": "Tennessee Titans",        "position": "WR",  "ig_handle": "deandrehopkins"},
    {"name": "Calvin Ridley",        "team": "Tennessee Titans",        "position": "WR",  "ig_handle": "calvinridley18"},
    {"name": "Tyler Boyd",           "team": "Tennessee Titans",        "position": "WR",  "ig_handle": "tylerboyd83"},
    {"name": "Tony Pollard",         "team": "Tennessee Titans",        "position": "RB",  "ig_handle": "tonypollard"},
    {"name": "Chigoziem Okonkwo",    "team": "Tennessee Titans",        "position": "TE",  "ig_handle": "chigoziemokonkwo"},
    {"name": "Harold Landry",        "team": "Tennessee Titans",        "position": "LB",  "ig_handle": "haroldlandry55"},
    {"name": "L'Jarius Sneed",       "team": "Tennessee Titans",        "position": "CB",  "ig_handle": "ljariussneed2"},
    {"name": "Jeffery Simmons",      "team": "Tennessee Titans",        "position": "DT",  "ig_handle": "jefferysimmons98"},

    # ════════════════════════════════════════════════════════════════════════
    # AFC WEST
    # ════════════════════════════════════════════════════════════════════════

    # ── Denver Broncos ────────────────────────────────────────────────────
    {"name": "Bo Nix",               "team": "Denver Broncos",          "position": "QB",  "ig_handle": "bonix10"},
    {"name": "Courtland Sutton",     "team": "Denver Broncos",          "position": "WR",  "ig_handle": "courtlandsutton"},
    {"name": "Troy Franklin",        "team": "Denver Broncos",          "position": "WR",  "ig_handle": "troyfranklin_"},
    {"name": "Greg Dulcich",         "team": "Denver Broncos",          "position": "TE",  "ig_handle": "greg_dulcich"},
    {"name": "Javonte Williams",     "team": "Denver Broncos",          "position": "RB",  "ig_handle": "javontewilliams33"},
    {"name": "Patrick Surtain II",   "team": "Denver Broncos",          "position": "CB",  "ig_handle": "psurtain_2"},
    {"name": "Justin Simmons",       "team": "Denver Broncos",          "position": "S",   "ig_handle": "jsimms1129"},
    {"name": "Jonathan Cooper",      "team": "Denver Broncos",          "position": "DE",  "ig_handle": "jcooper51"},
    {"name": "Zach Allen",           "team": "Denver Broncos",          "position": "DE",  "ig_handle": "zachallen94"},

    # ── Kansas City Chiefs ────────────────────────────────────────────────
    {"name": "Patrick Mahomes",      "team": "Kansas City Chiefs",      "position": "QB",  "ig_handle": "patrickmahomes"},
    {"name": "Travis Kelce",         "team": "Kansas City Chiefs",      "position": "TE",  "ig_handle": "killatrav"},
    {"name": "Rashee Rice",          "team": "Kansas City Chiefs",      "position": "WR",  "ig_handle": "rasheerice"},
    {"name": "Hollywood Brown",      "team": "Kansas City Chiefs",      "position": "WR",  "ig_handle": "hollywoodbrown1"},
    {"name": "Isiah Pacheco",        "team": "Kansas City Chiefs",      "position": "RB",  "ig_handle": "ipacheco10"},
    {"name": "Chris Jones",          "team": "Kansas City Chiefs",      "position": "DT",  "ig_handle": "ssjones95"},
    {"name": "Nick Bolton",          "team": "Kansas City Chiefs",      "position": "LB",  "ig_handle": "nickbolton32"},
    {"name": "Trent McDuffie",       "team": "Kansas City Chiefs",      "position": "CB",  "ig_handle": "trentmcduffie22"},
    {"name": "Justin Reid",          "team": "Kansas City Chiefs",      "position": "S",   "ig_handle": "justinreid20"},

    # ── Las Vegas Raiders ─────────────────────────────────────────────────
    {"name": "Gardner Minshew",      "team": "Las Vegas Raiders",       "position": "QB",  "ig_handle": "gardnerminshew5"},
    {"name": "Brock Bowers",         "team": "Las Vegas Raiders",       "position": "TE",  "ig_handle": "brockbowers89"},
    {"name": "Jakobi Meyers",        "team": "Las Vegas Raiders",       "position": "WR",  "ig_handle": "jakobimeyers16"},
    {"name": "Tre Tucker",           "team": "Las Vegas Raiders",       "position": "WR",  "ig_handle": "tretucker10"},
    {"name": "Alexander Mattison",   "team": "Las Vegas Raiders",       "position": "RB",  "ig_handle": "alexandermattison"},
    {"name": "Maxx Crosby",          "team": "Las Vegas Raiders",       "position": "DE",  "ig_handle": "maxxcrosby"},
    {"name": "Robert Spillane",      "team": "Las Vegas Raiders",       "position": "LB",  "ig_handle": "robertspillane"},
    {"name": "Nate Hobbs",           "team": "Las Vegas Raiders",       "position": "CB",  "ig_handle": "natehobbs22"},

    # ── Los Angeles Chargers ──────────────────────────────────────────────
    {"name": "Justin Herbert",       "team": "Los Angeles Chargers",    "position": "QB",  "ig_handle": "justinherbert"},
    {"name": "Quentin Johnston",     "team": "Los Angeles Chargers",    "position": "WR",  "ig_handle": "qjohnston1"},
    {"name": "Ladd McConkey",        "team": "Los Angeles Chargers",    "position": "WR",  "ig_handle": "laddmcconkey"},
    {"name": "Will Dissly",          "team": "Los Angeles Chargers",    "position": "TE",  "ig_handle": "willdissly"},
    {"name": "J.K. Dobbins",         "team": "Los Angeles Chargers",    "position": "RB",  "ig_handle": "jkdobbins22"},
    {"name": "Joey Bosa",            "team": "Los Angeles Chargers",    "position": "DE",  "ig_handle": "joeybosa99"},
    {"name": "Derwin James",         "team": "Los Angeles Chargers",    "position": "S",   "ig_handle": "derwinjames"},
    {"name": "Asante Samuel Jr.",    "team": "Los Angeles Chargers",    "position": "CB",  "ig_handle": "asante.samjr"},
    {"name": "Khalil Mack",          "team": "Los Angeles Chargers",    "position": "LB",  "ig_handle": "khalilmack52"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC EAST
    # ════════════════════════════════════════════════════════════════════════

    # ── Dallas Cowboys ────────────────────────────────────────────────────
    {"name": "Dak Prescott",         "team": "Dallas Cowboys",          "position": "QB",  "ig_handle": "_dak"},
    {"name": "CeeDee Lamb",          "team": "Dallas Cowboys",          "position": "WR",  "ig_handle": "cdliii"},
    {"name": "Brandin Cooks",        "team": "Dallas Cowboys",          "position": "WR",  "ig_handle": "brandincooks"},
    {"name": "Jake Ferguson",        "team": "Dallas Cowboys",          "position": "TE",  "ig_handle": "jakeferguson"},
    {"name": "Rico Dowdle",          "team": "Dallas Cowboys",          "position": "RB",  "ig_handle": "ricodownle"},
    {"name": "Micah Parsons",        "team": "Dallas Cowboys",          "position": "LB",  "ig_handle": "itsmicahparsons"},
    {"name": "Trevon Diggs",         "team": "Dallas Cowboys",          "position": "CB",  "ig_handle": "trevon.diggs"},
    {"name": "DeMarcus Lawrence",    "team": "Dallas Cowboys",          "position": "DE",  "ig_handle": "demarcuslawrence"},
    {"name": "DaRon Bland",          "team": "Dallas Cowboys",          "position": "CB",  "ig_handle": "daronbland"},

    # ── New York Giants ───────────────────────────────────────────────────
    {"name": "Daniel Jones",         "team": "New York Giants",         "position": "QB",  "ig_handle": "dannyj14"},
    {"name": "Malik Nabers",         "team": "New York Giants",         "position": "WR",  "ig_handle": "maliknabers1"},
    {"name": "Wan'Dale Robinson",    "team": "New York Giants",         "position": "WR",  "ig_handle": "wandalerobinson"},
    {"name": "Darius Slayton",       "team": "New York Giants",         "position": "WR",  "ig_handle": "dslayton26"},
    {"name": "Devin Singletary",     "team": "New York Giants",         "position": "RB",  "ig_handle": "general_26"},
    {"name": "Kayvon Thibodeaux",    "team": "New York Giants",         "position": "DE",  "ig_handle": "kvonthibodeaux5"},
    {"name": "Dexter Lawrence",      "team": "New York Giants",         "position": "DT",  "ig_handle": "dex4law"},
    {"name": "Xavier McKinney",      "team": "Green Bay Packers",       "position": "S",   "ig_handle": "xaviermckinney15"},

    # ── Philadelphia Eagles ───────────────────────────────────────────────
    {"name": "Jalen Hurts",          "team": "Philadelphia Eagles",     "position": "QB",  "ig_handle": "jalenhurts"},
    {"name": "A.J. Brown",           "team": "Philadelphia Eagles",     "position": "WR",  "ig_handle": "1randomkid_"},
    {"name": "DeVonta Smith",        "team": "Philadelphia Eagles",     "position": "WR",  "ig_handle": "devontasmith_6"},
    {"name": "Dallas Goedert",       "team": "Philadelphia Eagles",     "position": "TE",  "ig_handle": "dgoedert88"},
    {"name": "Saquon Barkley",       "team": "Philadelphia Eagles",     "position": "RB",  "ig_handle": "saquon"},
    {"name": "Jalen Carter",         "team": "Philadelphia Eagles",     "position": "DT",  "ig_handle": "jalencarter98"},
    {"name": "Haason Reddick",       "team": "Philadelphia Eagles",     "position": "LB",  "ig_handle": "haasonreddick7"},
    {"name": "Darius Slay",          "team": "Philadelphia Eagles",     "position": "CB",  "ig_handle": "bigplay24slay"},
    {"name": "Lane Johnson",         "team": "Philadelphia Eagles",     "position": "OT",  "ig_handle": "lanejohnson65"},

    # ── Washington Commanders ─────────────────────────────────────────────
    {"name": "Jayden Daniels",       "team": "Washington Commanders",   "position": "QB",  "ig_handle": "jaydandaniels5"},
    {"name": "Terry McLaurin",       "team": "Washington Commanders",   "position": "WR",  "ig_handle": "tdott11"},
    {"name": "Jahan Dotson",         "team": "Washington Commanders",   "position": "WR",  "ig_handle": "jahandotson1"},
    {"name": "Noah Brown",           "team": "Washington Commanders",   "position": "WR",  "ig_handle": "noahbrown87"},
    {"name": "Brian Robinson Jr.",   "team": "Washington Commanders",   "position": "RB",  "ig_handle": "brianrobinson8"},
    {"name": "Austin Ekeler",        "team": "Washington Commanders",   "position": "RB",  "ig_handle": "austinekeler"},
    {"name": "Daron Payne",          "team": "Washington Commanders",   "position": "DT",  "ig_handle": "daronpayne94"},
    {"name": "Bobby Wagner",         "team": "Washington Commanders",   "position": "LB",  "ig_handle": "bobbywagner54"},
    {"name": "Emmanuel Forbes",      "team": "Washington Commanders",   "position": "CB",  "ig_handle": "emmanuelforbes"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC NORTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Chicago Bears ─────────────────────────────────────────────────────
    {"name": "Caleb Williams",       "team": "Chicago Bears",           "position": "QB",  "ig_handle": "calebwilliams"},
    {"name": "Keenan Allen",         "team": "Chicago Bears",           "position": "WR",  "ig_handle": "keenanallen13"},
    {"name": "DJ Moore",             "team": "Chicago Bears",           "position": "WR",  "ig_handle": "djmoore2"},
    {"name": "Rome Odunze",          "team": "Chicago Bears",           "position": "WR",  "ig_handle": "romeodunze"},
    {"name": "Cole Kmet",            "team": "Chicago Bears",           "position": "TE",  "ig_handle": "cole_kmet"},
    {"name": "D'Andre Swift",        "team": "Chicago Bears",           "position": "RB",  "ig_handle": "dandreswift"},
    {"name": "Montez Sweat",         "team": "Chicago Bears",           "position": "DE",  "ig_handle": "montezsweat9"},
    {"name": "Tremaine Edmunds",     "team": "Chicago Bears",           "position": "LB",  "ig_handle": "tremaineedmunds49"},
    {"name": "Jaylon Johnson",       "team": "Chicago Bears",           "position": "CB",  "ig_handle": "jaylonj2"},

    # ── Detroit Lions ─────────────────────────────────────────────────────
    {"name": "Jared Goff",           "team": "Detroit Lions",           "position": "QB",  "ig_handle": "jaredgoff16"},
    {"name": "Amon-Ra St. Brown",    "team": "Detroit Lions",           "position": "WR",  "ig_handle": "amonrastbrown"},
    {"name": "Jameson Williams",     "team": "Detroit Lions",           "position": "WR",  "ig_handle": "jamesonwilliams_2"},
    {"name": "Sam LaPorta",          "team": "Detroit Lions",           "position": "TE",  "ig_handle": "samla_porta"},
    {"name": "Jahmyr Gibbs",         "team": "Detroit Lions",           "position": "RB",  "ig_handle": "jahmyrgibbs"},
    {"name": "David Montgomery",     "team": "Detroit Lions",           "position": "RB",  "ig_handle": "davidmontgomery5"},
    {"name": "Aidan Hutchinson",     "team": "Detroit Lions",           "position": "DE",  "ig_handle": "aidanhutchinson"},
    {"name": "Kerby Joseph",         "team": "Detroit Lions",           "position": "S",   "ig_handle": "kerbyjoseph"},
    {"name": "Carlton Davis",        "team": "Detroit Lions",           "position": "CB",  "ig_handle": "carltondavis3"},

    # ── Green Bay Packers ─────────────────────────────────────────────────
    {"name": "Jordan Love",          "team": "Green Bay Packers",       "position": "QB",  "ig_handle": "jordan3love"},
    {"name": "Jayden Reed",          "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "jaydenreed11"},
    {"name": "Romeo Doubs",          "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "romeo.doubs"},
    {"name": "Christian Watson",     "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "christianwatson81"},
    {"name": "Tucker Kraft",         "team": "Green Bay Packers",       "position": "TE",  "ig_handle": "tuckerkraft"},
    {"name": "Josh Jacobs",          "team": "Green Bay Packers",       "position": "RB",  "ig_handle": "iamjoshjacobs"},
    {"name": "Jaire Alexander",      "team": "Green Bay Packers",       "position": "CB",  "ig_handle": "jairealexander23"},
    {"name": "Quay Walker",          "team": "Green Bay Packers",       "position": "LB",  "ig_handle": "quaywalker10"},
    {"name": "Devonte Wyatt",        "team": "Green Bay Packers",       "position": "DT",  "ig_handle": "devontewyatt"},

    # ── Minnesota Vikings ─────────────────────────────────────────────────
    {"name": "Sam Darnold",          "team": "Minnesota Vikings",       "position": "QB",  "ig_handle": "samdarnold14"},
    {"name": "Justin Jefferson",     "team": "Minnesota Vikings",       "position": "WR",  "ig_handle": "justinjefferson"},
    {"name": "Jordan Addison",       "team": "Minnesota Vikings",       "position": "WR",  "ig_handle": "jordanaddison2"},
    {"name": "T.J. Hockenson",       "team": "Minnesota Vikings",       "position": "TE",  "ig_handle": "tjhockenson"},
    {"name": "Aaron Jones",          "team": "Minnesota Vikings",       "position": "RB",  "ig_handle": "showtyme33_aj"},
    {"name": "Jonathan Greenard",    "team": "Minnesota Vikings",       "position": "DE",  "ig_handle": "jgreenard"},
    {"name": "Harrison Smith",       "team": "Minnesota Vikings",       "position": "S",   "ig_handle": "harrisonsmith22"},
    {"name": "Byron Murphy",         "team": "Minnesota Vikings",       "position": "CB",  "ig_handle": "byronmurphy"},
    {"name": "Andrew Van Ginkel",    "team": "Minnesota Vikings",       "position": "LB",  "ig_handle": "andrewvanginkel"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC SOUTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Atlanta Falcons ───────────────────────────────────────────────────
    {"name": "Kirk Cousins",         "team": "Atlanta Falcons",         "position": "QB",  "ig_handle": "kirkcousins8"},
    {"name": "Drake London",         "team": "Atlanta Falcons",         "position": "WR",  "ig_handle": "drakelo44"},
    {"name": "Darnell Mooney",       "team": "Atlanta Falcons",         "position": "WR",  "ig_handle": "darnellmooney11"},
    {"name": "Kyle Pitts",           "team": "Atlanta Falcons",         "position": "TE",  "ig_handle": "kylepitts88"},
    {"name": "Bijan Robinson",       "team": "Atlanta Falcons",         "position": "RB",  "ig_handle": "bijan4robinson"},
    {"name": "Tyler Allgeier",       "team": "Atlanta Falcons",         "position": "RB",  "ig_handle": "tylerallgeier"},
    {"name": "Matthew Judon",        "team": "Atlanta Falcons",         "position": "LB",  "ig_handle": "mattjudon"},
    {"name": "A.J. Terrell",         "team": "Atlanta Falcons",         "position": "CB",  "ig_handle": "aj_terrell8"},
    {"name": "Jessie Bates III",     "team": "Atlanta Falcons",         "position": "S",   "ig_handle": "jessiebates"},

    # ── Carolina Panthers ─────────────────────────────────────────────────
    {"name": "Bryce Young",          "team": "Carolina Panthers",       "position": "QB",  "ig_handle": "bryceyoung"},
    {"name": "Adam Thielen",         "team": "Carolina Panthers",       "position": "WR",  "ig_handle": "adamthielen19"},
    {"name": "Diontae Johnson",      "team": "Carolina Panthers",       "position": "WR",  "ig_handle": "diontaejohnson18"},
    {"name": "Hayden Hurst",         "team": "Carolina Panthers",       "position": "TE",  "ig_handle": "haydenhurst"},
    {"name": "Chuba Hubbard",        "team": "Carolina Panthers",       "position": "RB",  "ig_handle": "chubahubbard"},
    {"name": "Miles Sanders",        "team": "Carolina Panthers",       "position": "RB",  "ig_handle": "milesdontmiss"},
    {"name": "Brian Burns",          "team": "Carolina Panthers",       "position": "DE",  "ig_handle": "brianburns"},
    {"name": "Derrick Brown",        "team": "Carolina Panthers",       "position": "DT",  "ig_handle": "derrickbrown5"},
    {"name": "Jaycee Horn",          "team": "Carolina Panthers",       "position": "CB",  "ig_handle": "jayceehorn"},

    # ── New Orleans Saints ────────────────────────────────────────────────
    {"name": "Derek Carr",           "team": "New Orleans Saints",      "position": "QB",  "ig_handle": "derekcarrqb4"},
    {"name": "Chris Olave",          "team": "New Orleans Saints",      "position": "WR",  "ig_handle": "chrisolave_"},
    {"name": "Rashid Shaheed",       "team": "New Orleans Saints",      "position": "WR",  "ig_handle": "rashidshaheed"},
    {"name": "Juwan Johnson",        "team": "New Orleans Saints",      "position": "TE",  "ig_handle": "juwanjohnson"},
    {"name": "Alvin Kamara",         "team": "New Orleans Saints",      "position": "RB",  "ig_handle": "alvinkamara41"},
    {"name": "Cameron Jordan",       "team": "New Orleans Saints",      "position": "DE",  "ig_handle": "camjordan94"},
    {"name": "Marshon Lattimore",    "team": "New Orleans Saints",      "position": "CB",  "ig_handle": "marshawnlattimore"},
    {"name": "Tyrann Mathieu",       "team": "New Orleans Saints",      "position": "S",   "ig_handle": "tyrannmathieu32"},
    {"name": "Pete Werner",          "team": "New Orleans Saints",      "position": "LB",  "ig_handle": "petewerner"},

    # ── Tampa Bay Buccaneers ──────────────────────────────────────────────
    {"name": "Baker Mayfield",       "team": "Tampa Bay Buccaneers",    "position": "QB",  "ig_handle": "bakermayfield"},
    {"name": "Mike Evans",           "team": "Tampa Bay Buccaneers",    "position": "WR",  "ig_handle": "mr_evans13"},
    {"name": "Chris Godwin",         "team": "Tampa Bay Buccaneers",    "position": "WR",  "ig_handle": "cgodwin14"},
    {"name": "Cade Otton",           "team": "Tampa Bay Buccaneers",    "position": "TE",  "ig_handle": "cadeotton"},
    {"name": "Rachaad White",        "team": "Tampa Bay Buccaneers",    "position": "RB",  "ig_handle": "rachaadwhite"},
    {"name": "Bucky Irving",         "team": "Tampa Bay Buccaneers",    "position": "RB",  "ig_handle": "buckyirving"},
    {"name": "Vita Vea",             "team": "Tampa Bay Buccaneers",    "position": "DT",  "ig_handle": "vitavea75"},
    {"name": "Lavonte David",        "team": "Tampa Bay Buccaneers",    "position": "LB",  "ig_handle": "lavontedavid54"},
    {"name": "Antoine Winfield Jr.", "team": "Tampa Bay Buccaneers",    "position": "S",   "ig_handle": "antoinewingfield"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC WEST
    # ════════════════════════════════════════════════════════════════════════

    # ── Arizona Cardinals ────────────────────────────────────────────────
    {"name": "Kyler Murray",         "team": "Arizona Cardinals",       "position": "QB",  "ig_handle": "kyler1murray"},
    {"name": "Marvin Harrison Jr.",  "team": "Arizona Cardinals",       "position": "WR",  "ig_handle": "marvharrisonjr"},
    {"name": "Michael Wilson",       "team": "Arizona Cardinals",       "position": "WR",  "ig_handle": "michaelwilson3"},
    {"name": "Trey McBride",         "team": "Arizona Cardinals",       "position": "TE",  "ig_handle": "treymcbride85"},
    {"name": "James Conner",         "team": "Arizona Cardinals",       "position": "RB",  "ig_handle": "realcontact30"},
    {"name": "Budda Baker",          "team": "Arizona Cardinals",       "position": "S",   "ig_handle": "buddabaker32"},
    {"name": "Zaven Collins",        "team": "Arizona Cardinals",       "position": "LB",  "ig_handle": "zavencollins"},
    {"name": "Bilal Nichols",        "team": "Arizona Cardinals",       "position": "DT",  "ig_handle": "bilalnichols98"},
    {"name": "Kei'Trel Clark",       "team": "Arizona Cardinals",       "position": "CB",  "ig_handle": "keitrelclark"},

    # ── Los Angeles Rams ──────────────────────────────────────────────────
    {"name": "Matthew Stafford",     "team": "Los Angeles Rams",        "position": "QB",  "ig_handle": "matthewstafford9"},
    {"name": "Cooper Kupp",          "team": "Los Angeles Rams",        "position": "WR",  "ig_handle": "cooperkupp"},
    {"name": "Puka Nacua",           "team": "Los Angeles Rams",        "position": "WR",  "ig_handle": "pukanacua17"},
    {"name": "Tyler Higbee",         "team": "Los Angeles Rams",        "position": "TE",  "ig_handle": "tylerhigbee89"},
    {"name": "Kyren Williams",       "team": "Los Angeles Rams",        "position": "RB",  "ig_handle": "kyrenwilliams"},
    {"name": "Jared Verse",          "team": "Los Angeles Rams",        "position": "DE",  "ig_handle": "jaredverse"},
    {"name": "Byron Young",          "team": "Los Angeles Rams",        "position": "DE",  "ig_handle": "byronyoung"},
    {"name": "Darious Williams",     "team": "Los Angeles Rams",        "position": "CB",  "ig_handle": "dariouswilliams"},
    {"name": "Jordan Fuller",        "team": "Los Angeles Rams",        "position": "S",   "ig_handle": "jordanfuller"},

    # ── San Francisco 49ers ───────────────────────────────────────────────
    {"name": "Brock Purdy",          "team": "San Francisco 49ers",     "position": "QB",  "ig_handle": "brockpurdy13"},
    {"name": "Deebo Samuel",         "team": "San Francisco 49ers",     "position": "WR",  "ig_handle": "debo"},
    {"name": "Brandon Aiyuk",        "team": "San Francisco 49ers",     "position": "WR",  "ig_handle": "_brandonaiyuk"},
    {"name": "George Kittle",        "team": "San Francisco 49ers",     "position": "TE",  "ig_handle": "gkittle46"},
    {"name": "Christian McCaffrey",  "team": "San Francisco 49ers",     "position": "RB",  "ig_handle": "christianmccaffrey"},
    {"name": "Jordan Mason",         "team": "San Francisco 49ers",     "position": "RB",  "ig_handle": "jordanmason24"},
    {"name": "Nick Bosa",            "team": "San Francisco 49ers",     "position": "DE",  "ig_handle": "nbsmallerbear"},
    {"name": "Fred Warner",          "team": "San Francisco 49ers",     "position": "LB",  "ig_handle": "fredwarner"},
    {"name": "Charvarius Ward",      "team": "San Francisco 49ers",     "position": "CB",  "ig_handle": "manhuntward21"},
    {"name": "Trent Williams",       "team": "San Francisco 49ers",     "position": "OT",  "ig_handle": "trent"},
    {"name": "Talanoa Hufanga",      "team": "San Francisco 49ers",     "position": "S",   "ig_handle": "talanoahufanga"},

    # ── Seattle Seahawks ──────────────────────────────────────────────────
    {"name": "Geno Smith",           "team": "Seattle Seahawks",        "position": "QB",  "ig_handle": "genosmith7"},
    {"name": "DK Metcalf",           "team": "Seattle Seahawks",        "position": "WR",  "ig_handle": "dkmetcalf14"},
    {"name": "Tyler Lockett",        "team": "Seattle Seahawks",        "position": "WR",  "ig_handle": "tlockett16"},
    {"name": "Noah Fant",            "team": "Seattle Seahawks",        "position": "TE",  "ig_handle": "noahfant"},
    {"name": "Kenneth Walker III",   "team": "Seattle Seahawks",        "position": "RB",  "ig_handle": "kennywalker22"},
    {"name": "Uchenna Nwosu",        "team": "Seattle Seahawks",        "position": "LB",  "ig_handle": "uchennanwosu"},
    {"name": "Tariq Woolen",         "team": "Seattle Seahawks",        "position": "CB",  "ig_handle": "tariqwoolen"},
    {"name": "Quandre Diggs",        "team": "Seattle Seahawks",        "position": "S",   "ig_handle": "quandrediggs"},
    {"name": "Leonard Williams",     "team": "Seattle Seahawks",        "position": "DT",  "ig_handle": "leonardwilliams99"},
]


def seed_players():
    """Populate the players table. Safe to run multiple times."""
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
