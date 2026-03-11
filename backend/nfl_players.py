"""
NFL players seed data — best-effort Instagram handles as of early 2025.
Approximately 450 players across all 32 teams (~14 per team).
The tracker logs a warning and skips any handle that doesn't resolve on Instagram;
it's safe to re-run seed_players() after adding or correcting entries.
"""

from backend.database import upsert_player

NFL_PLAYERS = [

    # ════════════════════════════════════════════════════════════════════════
    # AFC EAST
    # ════════════════════════════════════════════════════════════════════════

    # ── Buffalo Bills ─────────────────────────────────────────────────────
    {"name": "Josh Allen",             "team": "Buffalo Bills",           "position": "QB",  "ig_handle": "joshallenqb"},
    {"name": "Mitchell Trubisky",      "team": "Buffalo Bills",           "position": "QB",  "ig_handle": "mitch_trubisky"},
    {"name": "Keon Coleman",           "team": "Buffalo Bills",           "position": "WR",  "ig_handle": "keoncoleman22"},
    {"name": "Khalil Shakir",          "team": "Buffalo Bills",           "position": "WR",  "ig_handle": "khalilshakir"},
    {"name": "Curtis Samuel",          "team": "Buffalo Bills",           "position": "WR",  "ig_handle": "curtissamuel10"},
    {"name": "Dawson Knox",            "team": "Buffalo Bills",           "position": "TE",  "ig_handle": "dawsonknox"},
    {"name": "James Cook",             "team": "Buffalo Bills",           "position": "RB",  "ig_handle": "jamescook"},
    {"name": "Ray Davis",              "team": "Buffalo Bills",           "position": "RB",  "ig_handle": "raydavis23"},
    {"name": "Dion Dawkins",           "team": "Buffalo Bills",           "position": "OT",  "ig_handle": "diondawkins73"},
    {"name": "Damar Hamlin",           "team": "Buffalo Bills",           "position": "S",   "ig_handle": "damarhamlin3"},
    {"name": "Taron Johnson",          "team": "Buffalo Bills",           "position": "CB",  "ig_handle": "taronj22"},
    {"name": "Ed Oliver",              "team": "Buffalo Bills",           "position": "DT",  "ig_handle": "edoliver91"},
    {"name": "Gregory Rousseau",       "team": "Buffalo Bills",           "position": "DE",  "ig_handle": "gregoryrousseau"},
    {"name": "AJ Epenesa",             "team": "Buffalo Bills",           "position": "DE",  "ig_handle": "ajepenesa57"},

    # ── Miami Dolphins ────────────────────────────────────────────────────
    {"name": "Tua Tagovailoa",         "team": "Miami Dolphins",          "position": "QB",  "ig_handle": "tuatagovailoa"},
    {"name": "Skylar Thompson",        "team": "Miami Dolphins",          "position": "QB",  "ig_handle": "skylarthompson"},
    {"name": "Tyreek Hill",            "team": "Miami Dolphins",          "position": "WR",  "ig_handle": "cheetah"},
    {"name": "Jaylen Waddle",          "team": "Miami Dolphins",          "position": "WR",  "ig_handle": "jaywaddle17"},
    {"name": "Odell Beckham Jr.",      "team": "Miami Dolphins",          "position": "WR",  "ig_handle": "obj"},
    {"name": "Jonnu Smith",            "team": "Miami Dolphins",          "position": "TE",  "ig_handle": "jonnusmith"},
    {"name": "De'Von Achane",          "team": "Miami Dolphins",          "position": "RB",  "ig_handle": "devon_achane6"},
    {"name": "Raheem Mostert",         "team": "Miami Dolphins",          "position": "RB",  "ig_handle": "raheemmostert31"},
    {"name": "Terron Armstead",        "team": "Miami Dolphins",          "position": "OT",  "ig_handle": "terronarmstead72"},
    {"name": "Jalen Ramsey",           "team": "Miami Dolphins",          "position": "CB",  "ig_handle": "jalenramsey"},
    {"name": "Xavien Howard",          "team": "Miami Dolphins",          "position": "CB",  "ig_handle": "xavienhoward25"},
    {"name": "Jevon Holland",          "team": "Miami Dolphins",          "position": "S",   "ig_handle": "jevonholland"},
    {"name": "Bradley Chubb",          "team": "Miami Dolphins",          "position": "LB",  "ig_handle": "bradleychubb2"},
    {"name": "Emmanuel Ogbah",         "team": "Miami Dolphins",          "position": "DE",  "ig_handle": "emmanuelogbah"},

    # ── New England Patriots ──────────────────────────────────────────────
    {"name": "Drake Maye",             "team": "New England Patriots",    "position": "QB",  "ig_handle": "drakemaye10"},
    {"name": "Jacoby Brissett",        "team": "New England Patriots",    "position": "QB",  "ig_handle": "jacobybrissett"},
    {"name": "Kendrick Bourne",        "team": "New England Patriots",    "position": "WR",  "ig_handle": "ktbourne11"},
    {"name": "DeMario Douglas",        "team": "New England Patriots",    "position": "WR",  "ig_handle": "demariodouglas"},
    {"name": "K.J. Osborn",            "team": "New England Patriots",    "position": "WR",  "ig_handle": "kjosborn17"},
    {"name": "Hunter Henry",           "team": "New England Patriots",    "position": "TE",  "ig_handle": "hunterhenry89"},
    {"name": "Rhamondre Stevenson",    "team": "New England Patriots",    "position": "RB",  "ig_handle": "rhamondre21"},
    {"name": "Antonio Gibson",         "team": "New England Patriots",    "position": "RB",  "ig_handle": "antoniogibson"},
    {"name": "Christian Barmore",      "team": "New England Patriots",    "position": "DT",  "ig_handle": "christianbarmore"},
    {"name": "Ja'Whaun Bentley",       "team": "New England Patriots",    "position": "LB",  "ig_handle": "jawhaunbentley"},
    {"name": "Josh Uche",              "team": "New England Patriots",    "position": "LB",  "ig_handle": "joshuche"},
    {"name": "Jonathan Jones",         "team": "New England Patriots",    "position": "CB",  "ig_handle": "jjonescb"},
    {"name": "Marcus Jones",           "team": "New England Patriots",    "position": "CB",  "ig_handle": "marcusjones"},

    # ── New York Jets ─────────────────────────────────────────────────────
    {"name": "Aaron Rodgers",          "team": "New York Jets",           "position": "QB",  "ig_handle": "aaronrodgers12"},
    {"name": "Tyrod Taylor",           "team": "New York Jets",           "position": "QB",  "ig_handle": "tyrodtaylor"},
    {"name": "Garrett Wilson",         "team": "New York Jets",           "position": "WR",  "ig_handle": "garrettwilson5"},
    {"name": "Davante Adams",          "team": "New York Jets",           "position": "WR",  "ig_handle": "tae15adams"},
    {"name": "Allen Lazard",           "team": "New York Jets",           "position": "WR",  "ig_handle": "allenlazard"},
    {"name": "Tyler Conklin",          "team": "New York Jets",           "position": "TE",  "ig_handle": "tylerconklin83"},
    {"name": "Breece Hall",            "team": "New York Jets",           "position": "RB",  "ig_handle": "breecehall20"},
    {"name": "Isaiah Davis",           "team": "New York Jets",           "position": "RB",  "ig_handle": "isaiahd"},
    {"name": "Sauce Gardner",          "team": "New York Jets",           "position": "CB",  "ig_handle": "iamsauce_gardner"},
    {"name": "D.J. Reed",              "team": "New York Jets",           "position": "CB",  "ig_handle": "djreed4"},
    {"name": "Jordan Whitehead",       "team": "New York Jets",           "position": "S",   "ig_handle": "jwhitehead9"},
    {"name": "Haason Reddick",         "team": "New York Jets",           "position": "LB",  "ig_handle": "haasonreddick7"},
    {"name": "Quinnen Williams",       "team": "New York Jets",           "position": "DT",  "ig_handle": "quinnenwilliams95"},
    {"name": "Will McDonald IV",       "team": "New York Jets",           "position": "DE",  "ig_handle": "willmcdonald4"},
    {"name": "C.J. Mosley",            "team": "New York Jets",           "position": "LB",  "ig_handle": "cjmosley57"},

    # ════════════════════════════════════════════════════════════════════════
    # AFC NORTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Baltimore Ravens ──────────────────────────────────────────────────
    {"name": "Lamar Jackson",          "team": "Baltimore Ravens",        "position": "QB",  "ig_handle": "lj_era8"},
    {"name": "Zay Flowers",            "team": "Baltimore Ravens",        "position": "WR",  "ig_handle": "zayflowers4"},
    {"name": "Nelson Agholor",         "team": "Baltimore Ravens",        "position": "WR",  "ig_handle": "nelsonagholor"},
    {"name": "Rashod Bateman",         "team": "Baltimore Ravens",        "position": "WR",  "ig_handle": "rashodbateman"},
    {"name": "Mark Andrews",           "team": "Baltimore Ravens",        "position": "TE",  "ig_handle": "markandrews"},
    {"name": "Isaiah Likely",          "team": "Baltimore Ravens",        "position": "TE",  "ig_handle": "isaiahlikely"},
    {"name": "Derrick Henry",          "team": "Baltimore Ravens",        "position": "RB",  "ig_handle": "kinghenry_2"},
    {"name": "Justice Hill",           "team": "Baltimore Ravens",        "position": "RB",  "ig_handle": "justicehill"},
    {"name": "Ronnie Stanley",         "team": "Baltimore Ravens",        "position": "OT",  "ig_handle": "ronniestanley"},
    {"name": "Roquan Smith",           "team": "Baltimore Ravens",        "position": "LB",  "ig_handle": "roquan_smith0"},
    {"name": "Kyle Hamilton",          "team": "Baltimore Ravens",        "position": "S",   "ig_handle": "kylehamilton"},
    {"name": "Marlon Humphrey",        "team": "Baltimore Ravens",        "position": "CB",  "ig_handle": "marlonhumphrey"},
    {"name": "Justin Madubuike",       "team": "Baltimore Ravens",        "position": "DT",  "ig_handle": "justinmadubuike"},
    {"name": "Odafe Oweh",             "team": "Baltimore Ravens",        "position": "LB",  "ig_handle": "odafeoweh"},

    # ── Cincinnati Bengals ────────────────────────────────────────────────
    {"name": "Joe Burrow",             "team": "Cincinnati Bengals",      "position": "QB",  "ig_handle": "joeburrow9"},
    {"name": "Jake Browning",          "team": "Cincinnati Bengals",      "position": "QB",  "ig_handle": "jakebrowning3"},
    {"name": "Ja'Marr Chase",          "team": "Cincinnati Bengals",      "position": "WR",  "ig_handle": "real10ja"},
    {"name": "Tee Higgins",            "team": "Cincinnati Bengals",      "position": "WR",  "ig_handle": "teehiggins5"},
    {"name": "Charlie Jones",          "team": "Cincinnati Bengals",      "position": "WR",  "ig_handle": "charliejones"},
    {"name": "Mike Gesicki",           "team": "Cincinnati Bengals",      "position": "TE",  "ig_handle": "mikegesicki88"},
    {"name": "Chase Brown",            "team": "Cincinnati Bengals",      "position": "RB",  "ig_handle": "chasebrown"},
    {"name": "Zack Moss",              "team": "Cincinnati Bengals",      "position": "RB",  "ig_handle": "zackmoss"},
    {"name": "Orlando Brown Jr.",      "team": "Cincinnati Bengals",      "position": "OT",  "ig_handle": "orlandobrown"},
    {"name": "Trey Hendrickson",       "team": "Cincinnati Bengals",      "position": "DE",  "ig_handle": "treyhendrickson"},
    {"name": "Sam Hubbard",            "team": "Cincinnati Bengals",      "position": "DE",  "ig_handle": "samhubbard94"},
    {"name": "Cam Taylor-Britt",       "team": "Cincinnati Bengals",      "position": "CB",  "ig_handle": "camtaylorbritt"},
    {"name": "Dax Hill",               "team": "Cincinnati Bengals",      "position": "S",   "ig_handle": "daxhill"},
    {"name": "Logan Wilson",           "team": "Cincinnati Bengals",      "position": "LB",  "ig_handle": "loganwilson55"},

    # ── Cleveland Browns ──────────────────────────────────────────────────
    {"name": "Deshaun Watson",         "team": "Cleveland Browns",        "position": "QB",  "ig_handle": "deshaunwatson"},
    {"name": "Amari Cooper",           "team": "Cleveland Browns",        "position": "WR",  "ig_handle": "amaricooper9"},
    {"name": "Jerry Jeudy",            "team": "Cleveland Browns",        "position": "WR",  "ig_handle": "jerryjeudy"},
    {"name": "Elijah Moore",           "team": "Cleveland Browns",        "position": "WR",  "ig_handle": "elijahmoore"},
    {"name": "David Njoku",            "team": "Cleveland Browns",        "position": "TE",  "ig_handle": "davidnjoku_"},
    {"name": "Nick Chubb",             "team": "Cleveland Browns",        "position": "RB",  "ig_handle": "nickchubb21"},
    {"name": "Jerome Ford",            "team": "Cleveland Browns",        "position": "RB",  "ig_handle": "jeromeford"},
    {"name": "Jedrick Wills Jr.",      "team": "Cleveland Browns",        "position": "OT",  "ig_handle": "jedrickwills74"},
    {"name": "Myles Garrett",          "team": "Cleveland Browns",        "position": "DE",  "ig_handle": "flash_g2x"},
    {"name": "Za'Darius Smith",        "team": "Cleveland Browns",        "position": "LB",  "ig_handle": "zadariussmith55"},
    {"name": "Denzel Ward",            "team": "Cleveland Browns",        "position": "CB",  "ig_handle": "denzelward21"},
    {"name": "Juan Thornhill",         "team": "Cleveland Browns",        "position": "S",   "ig_handle": "juanthornhill22"},
    {"name": "Dalvin Tomlinson",       "team": "Cleveland Browns",        "position": "DT",  "ig_handle": "dalvintomlinson"},
    {"name": "Joe Flacco",             "team": "Cleveland Browns",        "position": "QB",  "ig_handle": "joeflacco5"},

    # ── Pittsburgh Steelers ───────────────────────────────────────────────
    {"name": "Russell Wilson",         "team": "Pittsburgh Steelers",     "position": "QB",  "ig_handle": "dangerrusswilson"},
    {"name": "Justin Fields",          "team": "Pittsburgh Steelers",     "position": "QB",  "ig_handle": "justnfields1"},
    {"name": "George Pickens",         "team": "Pittsburgh Steelers",     "position": "WR",  "ig_handle": "gee_pickens"},
    {"name": "Calvin Austin III",      "team": "Pittsburgh Steelers",     "position": "WR",  "ig_handle": "calvino3"},
    {"name": "Van Jefferson",          "team": "Pittsburgh Steelers",     "position": "WR",  "ig_handle": "vanjefferson"},
    {"name": "Pat Freiermuth",         "team": "Pittsburgh Steelers",     "position": "TE",  "ig_handle": "patfreiermuth"},
    {"name": "Najee Harris",           "team": "Pittsburgh Steelers",     "position": "RB",  "ig_handle": "najeeharris22"},
    {"name": "Jaylen Warren",          "team": "Pittsburgh Steelers",     "position": "RB",  "ig_handle": "jaylenwarren30"},
    {"name": "T.J. Watt",              "team": "Pittsburgh Steelers",     "position": "LB",  "ig_handle": "tj_watt"},
    {"name": "Alex Highsmith",         "team": "Pittsburgh Steelers",     "position": "LB",  "ig_handle": "alexhighsmith"},
    {"name": "Patrick Queen",          "team": "Pittsburgh Steelers",     "position": "LB",  "ig_handle": "patqueen6"},
    {"name": "Minkah Fitzpatrick",     "team": "Pittsburgh Steelers",     "position": "S",   "ig_handle": "minkah"},
    {"name": "Joey Porter Jr.",        "team": "Pittsburgh Steelers",     "position": "CB",  "ig_handle": "joeyporterjr"},
    {"name": "Cameron Heyward",        "team": "Pittsburgh Steelers",     "position": "DT",  "ig_handle": "camhey"},

    # ════════════════════════════════════════════════════════════════════════
    # AFC SOUTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Houston Texans ────────────────────────────────────────────────────
    {"name": "C.J. Stroud",            "team": "Houston Texans",          "position": "QB",  "ig_handle": "cj.stroud7"},
    {"name": "Case Keenum",            "team": "Houston Texans",          "position": "QB",  "ig_handle": "casekeenum7"},
    {"name": "Nico Collins",           "team": "Houston Texans",          "position": "WR",  "ig_handle": "nicocollins4"},
    {"name": "Tank Dell",              "team": "Houston Texans",          "position": "WR",  "ig_handle": "tankdell3"},
    {"name": "Stefon Diggs",           "team": "Houston Texans",          "position": "WR",  "ig_handle": "stefondiggs"},
    {"name": "Dalton Schultz",         "team": "Houston Texans",          "position": "TE",  "ig_handle": "dalton.schultz86"},
    {"name": "Joe Mixon",              "team": "Houston Texans",          "position": "RB",  "ig_handle": "joemixon21"},
    {"name": "Dameon Pierce",          "team": "Houston Texans",          "position": "RB",  "ig_handle": "dameonpierce31"},
    {"name": "Laremy Tunsil",          "team": "Houston Texans",          "position": "OT",  "ig_handle": "laremy78"},
    {"name": "Will Anderson Jr.",      "team": "Houston Texans",          "position": "DE",  "ig_handle": "willandersonjr"},
    {"name": "Danielle Hunter",        "team": "Houston Texans",          "position": "DE",  "ig_handle": "daniellehunter99"},
    {"name": "Derek Stingley Jr.",     "team": "Houston Texans",          "position": "CB",  "ig_handle": "derek_stingley2"},
    {"name": "Jalen Pitre",            "team": "Houston Texans",          "position": "S",   "ig_handle": "jalenpitre"},
    {"name": "Henry To'oTo'o",         "team": "Houston Texans",          "position": "LB",  "ig_handle": "henrytootoo"},

    # ── Indianapolis Colts ────────────────────────────────────────────────
    {"name": "Anthony Richardson",    "team": "Indianapolis Colts",      "position": "QB",  "ig_handle": "antr_5"},
    {"name": "Joe Flacco",             "team": "Indianapolis Colts",      "position": "QB",  "ig_handle": "joeflacco5"},
    {"name": "Michael Pittman Jr.",   "team": "Indianapolis Colts",      "position": "WR",  "ig_handle": "mpittmanjr"},
    {"name": "Josh Downs",             "team": "Indianapolis Colts",      "position": "WR",  "ig_handle": "joshuadowns9"},
    {"name": "Adonai Mitchell",        "team": "Indianapolis Colts",      "position": "WR",  "ig_handle": "adonaimitch"},
    {"name": "Mo Alie-Cox",            "team": "Indianapolis Colts",      "position": "TE",  "ig_handle": "moaliecox"},
    {"name": "Jonathan Taylor",        "team": "Indianapolis Colts",      "position": "RB",  "ig_handle": "jontaylor"},
    {"name": "Trey Sermon",            "team": "Indianapolis Colts",      "position": "RB",  "ig_handle": "treysermon"},
    {"name": "Bernhard Raimann",       "team": "Indianapolis Colts",      "position": "OT",  "ig_handle": "bernhardraimann"},
    {"name": "DeForest Buckner",       "team": "Indianapolis Colts",      "position": "DT",  "ig_handle": "deforest_buckner"},
    {"name": "Kwity Paye",             "team": "Indianapolis Colts",      "position": "DE",  "ig_handle": "kwitypaye"},
    {"name": "Zaire Franklin",         "team": "Indianapolis Colts",      "position": "LB",  "ig_handle": "zairefranklin"},
    {"name": "Kenny Moore II",         "team": "Indianapolis Colts",      "position": "CB",  "ig_handle": "kennymoore_2"},
    {"name": "Julian Blackmon",        "team": "Indianapolis Colts",      "position": "S",   "ig_handle": "juliandblackmon"},

    # ── Jacksonville Jaguars ──────────────────────────────────────────────
    {"name": "Trevor Lawrence",        "team": "Jacksonville Jaguars",    "position": "QB",  "ig_handle": "tlawrence16"},
    {"name": "Mac Jones",              "team": "Jacksonville Jaguars",    "position": "QB",  "ig_handle": "mac_jones10"},
    {"name": "Brian Thomas Jr.",       "team": "Jacksonville Jaguars",    "position": "WR",  "ig_handle": "brianthomaspwr"},
    {"name": "Christian Kirk",         "team": "Jacksonville Jaguars",    "position": "WR",  "ig_handle": "christiankirk"},
    {"name": "Gabe Davis",             "team": "Jacksonville Jaguars",    "position": "WR",  "ig_handle": "gabedavis"},
    {"name": "Evan Engram",            "team": "Jacksonville Jaguars",    "position": "TE",  "ig_handle": "evan_engram"},
    {"name": "Travis Etienne",         "team": "Jacksonville Jaguars",    "position": "RB",  "ig_handle": "travisetienne"},
    {"name": "Tank Bigsby",            "team": "Jacksonville Jaguars",    "position": "RB",  "ig_handle": "tankbigsby"},
    {"name": "Josh Allen",             "team": "Jacksonville Jaguars",    "position": "LB",  "ig_handle": "joshallen41_"},
    {"name": "Arik Armstead",          "team": "Jacksonville Jaguars",    "position": "DT",  "ig_handle": "arik_armstead"},
    {"name": "Devin Lloyd",            "team": "Jacksonville Jaguars",    "position": "LB",  "ig_handle": "devinlloyd"},
    {"name": "Tyson Campbell",         "team": "Jacksonville Jaguars",    "position": "CB",  "ig_handle": "tysoncampbell"},
    {"name": "Andre Cisco",            "team": "Jacksonville Jaguars",    "position": "S",   "ig_handle": "andrecisco"},
    {"name": "Darious Williams",       "team": "Jacksonville Jaguars",    "position": "CB",  "ig_handle": "dariouswilliams"},

    # ── Tennessee Titans ──────────────────────────────────────────────────
    {"name": "Will Levis",             "team": "Tennessee Titans",        "position": "QB",  "ig_handle": "willlevis"},
    {"name": "Mason Rudolph",          "team": "Tennessee Titans",        "position": "QB",  "ig_handle": "masonrudolph2"},
    {"name": "DeAndre Hopkins",        "team": "Tennessee Titans",        "position": "WR",  "ig_handle": "deandrehopkins"},
    {"name": "Calvin Ridley",          "team": "Tennessee Titans",        "position": "WR",  "ig_handle": "calvinridley18"},
    {"name": "Nick Westbrook-Ikhine",  "team": "Tennessee Titans",        "position": "WR",  "ig_handle": "nwestbrook1"},
    {"name": "Chigoziem Okonkwo",      "team": "Tennessee Titans",        "position": "TE",  "ig_handle": "chigoziemokonkwo"},
    {"name": "Tony Pollard",           "team": "Tennessee Titans",        "position": "RB",  "ig_handle": "tonypollard"},
    {"name": "Tyjae Spears",           "team": "Tennessee Titans",        "position": "RB",  "ig_handle": "tyjaespears"},
    {"name": "Harold Landry",          "team": "Tennessee Titans",        "position": "LB",  "ig_handle": "haroldlandry55"},
    {"name": "Jeffery Simmons",        "team": "Tennessee Titans",        "position": "DT",  "ig_handle": "jefferysimmons98"},
    {"name": "L'Jarius Sneed",         "team": "Tennessee Titans",        "position": "CB",  "ig_handle": "ljariussneed2"},
    {"name": "Chidobe Awuzie",         "team": "Tennessee Titans",        "position": "CB",  "ig_handle": "chidobe"},
    {"name": "Amani Hooker",           "team": "Tennessee Titans",        "position": "S",   "ig_handle": "amanihooker"},
    {"name": "Azeez Al-Shaair",        "team": "Tennessee Titans",        "position": "LB",  "ig_handle": "azeezalshaair"},

    # ════════════════════════════════════════════════════════════════════════
    # AFC WEST
    # ════════════════════════════════════════════════════════════════════════

    # ── Denver Broncos ────────────────────────────────────────────────────
    {"name": "Bo Nix",                 "team": "Denver Broncos",          "position": "QB",  "ig_handle": "bonix10"},
    {"name": "Jarrett Stidham",        "team": "Denver Broncos",          "position": "QB",  "ig_handle": "jarrettstidham"},
    {"name": "Courtland Sutton",       "team": "Denver Broncos",          "position": "WR",  "ig_handle": "courtlandsutton"},
    {"name": "Troy Franklin",          "team": "Denver Broncos",          "position": "WR",  "ig_handle": "troyfranklin_"},
    {"name": "Marvin Mims Jr.",        "team": "Denver Broncos",          "position": "WR",  "ig_handle": "marvinmimsjr"},
    {"name": "Greg Dulcich",           "team": "Denver Broncos",          "position": "TE",  "ig_handle": "greg_dulcich"},
    {"name": "Javonte Williams",       "team": "Denver Broncos",          "position": "RB",  "ig_handle": "javontewilliams33"},
    {"name": "Audric Estime",          "team": "Denver Broncos",          "position": "RB",  "ig_handle": "audricestimejr"},
    {"name": "Garett Bolles",          "team": "Denver Broncos",          "position": "OT",  "ig_handle": "garettbolles76"},
    {"name": "Patrick Surtain II",     "team": "Denver Broncos",          "position": "CB",  "ig_handle": "psurtain_2"},
    {"name": "Riley Moss",             "team": "Denver Broncos",          "position": "CB",  "ig_handle": "rileymoss"},
    {"name": "Jonathon Cooper",        "team": "Denver Broncos",          "position": "DE",  "ig_handle": "jcooper51"},
    {"name": "Nik Bonitto",            "team": "Denver Broncos",          "position": "LB",  "ig_handle": "nikbonitto"},
    {"name": "Justin Simmons",         "team": "Denver Broncos",          "position": "S",   "ig_handle": "jsimms1129"},

    # ── Kansas City Chiefs ────────────────────────────────────────────────
    {"name": "Patrick Mahomes",        "team": "Kansas City Chiefs",      "position": "QB",  "ig_handle": "patrickmahomes"},
    {"name": "Blaine Gabbert",         "team": "Kansas City Chiefs",      "position": "QB",  "ig_handle": "blaingabbert"},
    {"name": "Travis Kelce",           "team": "Kansas City Chiefs",      "position": "TE",  "ig_handle": "killatrav"},
    {"name": "Rashee Rice",            "team": "Kansas City Chiefs",      "position": "WR",  "ig_handle": "rasheerice"},
    {"name": "Hollywood Brown",        "team": "Kansas City Chiefs",      "position": "WR",  "ig_handle": "hollywoodbrown1"},
    {"name": "Xavier Worthy",          "team": "Kansas City Chiefs",      "position": "WR",  "ig_handle": "xavierworthy"},
    {"name": "Noah Gray",              "team": "Kansas City Chiefs",      "position": "TE",  "ig_handle": "noahgray"},
    {"name": "Isiah Pacheco",          "team": "Kansas City Chiefs",      "position": "RB",  "ig_handle": "ipacheco10"},
    {"name": "Kareem Hunt",            "team": "Kansas City Chiefs",      "position": "RB",  "ig_handle": "kareemhunt7"},
    {"name": "Creed Humphrey",         "team": "Kansas City Chiefs",      "position": "C",   "ig_handle": "creedhumphrey"},
    {"name": "Chris Jones",            "team": "Kansas City Chiefs",      "position": "DT",  "ig_handle": "ssjones95"},
    {"name": "George Karlaftis",       "team": "Kansas City Chiefs",      "position": "DE",  "ig_handle": "georgekarlaftis"},
    {"name": "Nick Bolton",            "team": "Kansas City Chiefs",      "position": "LB",  "ig_handle": "nickbolton32"},
    {"name": "Trent McDuffie",         "team": "Kansas City Chiefs",      "position": "CB",  "ig_handle": "trentmcduffie22"},
    {"name": "Justin Reid",            "team": "Kansas City Chiefs",      "position": "S",   "ig_handle": "justinreid20"},

    # ── Las Vegas Raiders ─────────────────────────────────────────────────
    {"name": "Aidan O'Connell",        "team": "Las Vegas Raiders",       "position": "QB",  "ig_handle": "aidanocqb"},
    {"name": "Gardner Minshew",        "team": "Las Vegas Raiders",       "position": "QB",  "ig_handle": "gardnerminshew5"},
    {"name": "Brock Bowers",           "team": "Las Vegas Raiders",       "position": "TE",  "ig_handle": "brockbowers89"},
    {"name": "Jakobi Meyers",          "team": "Las Vegas Raiders",       "position": "WR",  "ig_handle": "jakobimeyers16"},
    {"name": "Tre Tucker",             "team": "Las Vegas Raiders",       "position": "WR",  "ig_handle": "tretucker10"},
    {"name": "Alexander Mattison",     "team": "Las Vegas Raiders",       "position": "RB",  "ig_handle": "alexandermattison"},
    {"name": "Zamir White",            "team": "Las Vegas Raiders",       "position": "RB",  "ig_handle": "zamirwhite"},
    {"name": "Kolton Miller",          "team": "Las Vegas Raiders",       "position": "OT",  "ig_handle": "koltonmiller74"},
    {"name": "Maxx Crosby",            "team": "Las Vegas Raiders",       "position": "DE",  "ig_handle": "maxxcrosby"},
    {"name": "Christian Wilkins",      "team": "Las Vegas Raiders",       "position": "DT",  "ig_handle": "christianwilkins97"},
    {"name": "Robert Spillane",        "team": "Las Vegas Raiders",       "position": "LB",  "ig_handle": "robertspillane"},
    {"name": "Nate Hobbs",             "team": "Las Vegas Raiders",       "position": "CB",  "ig_handle": "natehobbs22"},
    {"name": "Marcus Epps",            "team": "Las Vegas Raiders",       "position": "S",   "ig_handle": "mepps32"},

    # ── Los Angeles Chargers ──────────────────────────────────────────────
    {"name": "Justin Herbert",         "team": "Los Angeles Chargers",    "position": "QB",  "ig_handle": "justinherbert"},
    {"name": "Easton Stick",           "team": "Los Angeles Chargers",    "position": "QB",  "ig_handle": "eastonstick12"},
    {"name": "Quentin Johnston",       "team": "Los Angeles Chargers",    "position": "WR",  "ig_handle": "qjohnston1"},
    {"name": "Ladd McConkey",          "team": "Los Angeles Chargers",    "position": "WR",  "ig_handle": "laddmcconkey"},
    {"name": "Joshua Palmer",          "team": "Los Angeles Chargers",    "position": "WR",  "ig_handle": "joshuapalmer5"},
    {"name": "Will Dissly",            "team": "Los Angeles Chargers",    "position": "TE",  "ig_handle": "willdissly"},
    {"name": "J.K. Dobbins",           "team": "Los Angeles Chargers",    "position": "RB",  "ig_handle": "jkdobbins22"},
    {"name": "Gus Edwards",            "team": "Los Angeles Chargers",    "position": "RB",  "ig_handle": "gusedwards35"},
    {"name": "Rashawn Slater",         "team": "Los Angeles Chargers",    "position": "OT",  "ig_handle": "rashawnslater70"},
    {"name": "Joey Bosa",              "team": "Los Angeles Chargers",    "position": "DE",  "ig_handle": "joeybosa99"},
    {"name": "Khalil Mack",            "team": "Los Angeles Chargers",    "position": "LB",  "ig_handle": "khalilmack52"},
    {"name": "Derwin James",           "team": "Los Angeles Chargers",    "position": "S",   "ig_handle": "derwinjames"},
    {"name": "Asante Samuel Jr.",      "team": "Los Angeles Chargers",    "position": "CB",  "ig_handle": "asante.samjr"},
    {"name": "Ja'Sir Taylor",          "team": "Los Angeles Chargers",    "position": "CB",  "ig_handle": "jasirtaylor"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC EAST
    # ════════════════════════════════════════════════════════════════════════

    # ── Dallas Cowboys ────────────────────────────────────────────────────
    {"name": "Dak Prescott",           "team": "Dallas Cowboys",          "position": "QB",  "ig_handle": "_dak"},
    {"name": "Cooper Rush",            "team": "Dallas Cowboys",          "position": "QB",  "ig_handle": "cooperrush7"},
    {"name": "CeeDee Lamb",            "team": "Dallas Cowboys",          "position": "WR",  "ig_handle": "cdliii"},
    {"name": "Brandin Cooks",          "team": "Dallas Cowboys",          "position": "WR",  "ig_handle": "brandincooks"},
    {"name": "Jalen Tolbert",          "team": "Dallas Cowboys",          "position": "WR",  "ig_handle": "jalentolbert18"},
    {"name": "Jake Ferguson",          "team": "Dallas Cowboys",          "position": "TE",  "ig_handle": "jakeferguson"},
    {"name": "Rico Dowdle",            "team": "Dallas Cowboys",          "position": "RB",  "ig_handle": "ricodownle"},
    {"name": "Ezekiel Elliott",        "team": "Dallas Cowboys",          "position": "RB",  "ig_handle": "eze_elliott15"},
    {"name": "Tyron Smith",            "team": "Dallas Cowboys",          "position": "OT",  "ig_handle": "tyronsmith77"},
    {"name": "Micah Parsons",          "team": "Dallas Cowboys",          "position": "LB",  "ig_handle": "itsmicahparsons"},
    {"name": "DeMarcus Lawrence",      "team": "Dallas Cowboys",          "position": "DE",  "ig_handle": "demarcuslawrence"},
    {"name": "Osa Odighizuwa",         "team": "Dallas Cowboys",          "position": "DT",  "ig_handle": "osaodighizuwa"},
    {"name": "Trevon Diggs",           "team": "Dallas Cowboys",          "position": "CB",  "ig_handle": "trevon.diggs"},
    {"name": "DaRon Bland",            "team": "Dallas Cowboys",          "position": "CB",  "ig_handle": "daronbland"},
    {"name": "Malik Hooker",           "team": "Dallas Cowboys",          "position": "S",   "ig_handle": "mhooker24"},

    # ── New York Giants ───────────────────────────────────────────────────
    {"name": "Daniel Jones",           "team": "New York Giants",         "position": "QB",  "ig_handle": "dannyj14"},
    {"name": "Tommy DeVito",           "team": "New York Giants",         "position": "QB",  "ig_handle": "tommydevito9"},
    {"name": "Malik Nabers",           "team": "New York Giants",         "position": "WR",  "ig_handle": "maliknabers1"},
    {"name": "Wan'Dale Robinson",      "team": "New York Giants",         "position": "WR",  "ig_handle": "wandalerobinson"},
    {"name": "Darius Slayton",         "team": "New York Giants",         "position": "WR",  "ig_handle": "dslayton26"},
    {"name": "Darren Waller",          "team": "New York Giants",         "position": "TE",  "ig_handle": "mrgwaller"},
    {"name": "Devin Singletary",       "team": "New York Giants",         "position": "RB",  "ig_handle": "general_26"},
    {"name": "Eric Gray",              "team": "New York Giants",         "position": "RB",  "ig_handle": "ericgray23"},
    {"name": "Andrew Thomas",          "team": "New York Giants",         "position": "OT",  "ig_handle": "andrewthomas78"},
    {"name": "Kayvon Thibodeaux",      "team": "New York Giants",         "position": "DE",  "ig_handle": "kvonthibodeaux5"},
    {"name": "Dexter Lawrence",        "team": "New York Giants",         "position": "DT",  "ig_handle": "dex4law"},
    {"name": "Brian Burns",            "team": "New York Giants",         "position": "DE",  "ig_handle": "brianburns"},
    {"name": "Bobby Okereke",          "team": "New York Giants",         "position": "LB",  "ig_handle": "bobbyokereke"},
    {"name": "Adoree' Jackson",        "team": "New York Giants",         "position": "CB",  "ig_handle": "adoree_"},

    # ── Philadelphia Eagles ───────────────────────────────────────────────
    {"name": "Jalen Hurts",            "team": "Philadelphia Eagles",     "position": "QB",  "ig_handle": "jalenhurts"},
    {"name": "Kenny Pickett",          "team": "Philadelphia Eagles",     "position": "QB",  "ig_handle": "kennypickett8"},
    {"name": "A.J. Brown",             "team": "Philadelphia Eagles",     "position": "WR",  "ig_handle": "1randomkid_"},
    {"name": "DeVonta Smith",          "team": "Philadelphia Eagles",     "position": "WR",  "ig_handle": "devontasmith_6"},
    {"name": "Britain Covey",          "team": "Philadelphia Eagles",     "position": "WR",  "ig_handle": "britaincovey18"},
    {"name": "Dallas Goedert",         "team": "Philadelphia Eagles",     "position": "TE",  "ig_handle": "dgoedert88"},
    {"name": "Saquon Barkley",         "team": "Philadelphia Eagles",     "position": "RB",  "ig_handle": "saquon"},
    {"name": "Kenneth Gainwell",       "team": "Philadelphia Eagles",     "position": "RB",  "ig_handle": "kennethgainwell"},
    {"name": "Lane Johnson",           "team": "Philadelphia Eagles",     "position": "OT",  "ig_handle": "lanejohnson65"},
    {"name": "Jordan Mailata",         "team": "Philadelphia Eagles",     "position": "OT",  "ig_handle": "jordanmailata"},
    {"name": "Jalen Carter",           "team": "Philadelphia Eagles",     "position": "DT",  "ig_handle": "jalencarter98"},
    {"name": "Josh Sweat",             "team": "Philadelphia Eagles",     "position": "DE",  "ig_handle": "joshsweat"},
    {"name": "Darius Slay",            "team": "Philadelphia Eagles",     "position": "CB",  "ig_handle": "bigplay24slay"},
    {"name": "James Bradberry",        "team": "Philadelphia Eagles",     "position": "CB",  "ig_handle": "jbradberry1"},
    {"name": "C.J. Gardner-Johnson",   "team": "Philadelphia Eagles",     "position": "S",   "ig_handle": "ceedy_deuces"},

    # ── Washington Commanders ─────────────────────────────────────────────
    {"name": "Jayden Daniels",         "team": "Washington Commanders",   "position": "QB",  "ig_handle": "jaydandaniels5"},
    {"name": "Marcus Mariota",         "team": "Washington Commanders",   "position": "QB",  "ig_handle": "marcus_mariota"},
    {"name": "Terry McLaurin",         "team": "Washington Commanders",   "position": "WR",  "ig_handle": "tdott11"},
    {"name": "Jahan Dotson",           "team": "Washington Commanders",   "position": "WR",  "ig_handle": "jahandotson1"},
    {"name": "Noah Brown",             "team": "Washington Commanders",   "position": "WR",  "ig_handle": "noahbrown87"},
    {"name": "Zach Ertz",              "team": "Washington Commanders",   "position": "TE",  "ig_handle": "zertz86"},
    {"name": "Brian Robinson Jr.",     "team": "Washington Commanders",   "position": "RB",  "ig_handle": "brianrobinson8"},
    {"name": "Austin Ekeler",          "team": "Washington Commanders",   "position": "RB",  "ig_handle": "austinekeler"},
    {"name": "Sam Cosmi",              "team": "Washington Commanders",   "position": "OT",  "ig_handle": "samcosmi"},
    {"name": "Daron Payne",            "team": "Washington Commanders",   "position": "DT",  "ig_handle": "daronpayne94"},
    {"name": "Jonathan Allen",         "team": "Washington Commanders",   "position": "DT",  "ig_handle": "jonathanallen93"},
    {"name": "Bobby Wagner",           "team": "Washington Commanders",   "position": "LB",  "ig_handle": "bobbywagner54"},
    {"name": "Emmanuel Forbes",        "team": "Washington Commanders",   "position": "CB",  "ig_handle": "emmanuelforbes"},
    {"name": "Kamren Curl",            "team": "Washington Commanders",   "position": "S",   "ig_handle": "kamrencurl"},
    {"name": "Kendall Fuller",         "team": "Washington Commanders",   "position": "CB",  "ig_handle": "kendallfuller29"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC NORTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Chicago Bears ─────────────────────────────────────────────────────
    {"name": "Caleb Williams",         "team": "Chicago Bears",           "position": "QB",  "ig_handle": "calebwilliams"},
    {"name": "Tyson Bagent",           "team": "Chicago Bears",           "position": "QB",  "ig_handle": "tysonbagent"},
    {"name": "Keenan Allen",           "team": "Chicago Bears",           "position": "WR",  "ig_handle": "keenanallen13"},
    {"name": "DJ Moore",               "team": "Chicago Bears",           "position": "WR",  "ig_handle": "djmoore2"},
    {"name": "Rome Odunze",            "team": "Chicago Bears",           "position": "WR",  "ig_handle": "romeodunze"},
    {"name": "Cole Kmet",              "team": "Chicago Bears",           "position": "TE",  "ig_handle": "cole_kmet"},
    {"name": "D'Andre Swift",          "team": "Chicago Bears",           "position": "RB",  "ig_handle": "dandreswift"},
    {"name": "Khalil Herbert",         "team": "Chicago Bears",           "position": "RB",  "ig_handle": "khalilherbert"},
    {"name": "Braxton Jones",          "team": "Chicago Bears",           "position": "OT",  "ig_handle": "braxtonjones76"},
    {"name": "Montez Sweat",           "team": "Chicago Bears",           "position": "DE",  "ig_handle": "montezsweat9"},
    {"name": "Grady Jarrett",          "team": "Chicago Bears",           "position": "DT",  "ig_handle": "gradyjarrett"},
    {"name": "Tremaine Edmunds",       "team": "Chicago Bears",           "position": "LB",  "ig_handle": "tremaineedmunds49"},
    {"name": "Jaylon Johnson",         "team": "Chicago Bears",           "position": "CB",  "ig_handle": "jaylonj2"},
    {"name": "Kevin Byard",            "team": "Chicago Bears",           "position": "S",   "ig_handle": "byard31"},

    # ── Detroit Lions ─────────────────────────────────────────────────────
    {"name": "Jared Goff",             "team": "Detroit Lions",           "position": "QB",  "ig_handle": "jaredgoff16"},
    {"name": "Hendon Hooker",          "team": "Detroit Lions",           "position": "QB",  "ig_handle": "hendonhooker"},
    {"name": "Amon-Ra St. Brown",      "team": "Detroit Lions",           "position": "WR",  "ig_handle": "amonrastbrown"},
    {"name": "Jameson Williams",       "team": "Detroit Lions",           "position": "WR",  "ig_handle": "jamesonwilliams_2"},
    {"name": "Josh Reynolds",          "team": "Detroit Lions",           "position": "WR",  "ig_handle": "joshreynolds"},
    {"name": "Sam LaPorta",            "team": "Detroit Lions",           "position": "TE",  "ig_handle": "samla_porta"},
    {"name": "Jahmyr Gibbs",           "team": "Detroit Lions",           "position": "RB",  "ig_handle": "jahmyrgibbs"},
    {"name": "David Montgomery",       "team": "Detroit Lions",           "position": "RB",  "ig_handle": "davidmontgomery5"},
    {"name": "Penei Sewell",           "team": "Detroit Lions",           "position": "OT",  "ig_handle": "peneisewell"},
    {"name": "Aidan Hutchinson",       "team": "Detroit Lions",           "position": "DE",  "ig_handle": "aidanhutchinson"},
    {"name": "Alim McNeill",           "team": "Detroit Lions",           "position": "DT",  "ig_handle": "alimmcneill"},
    {"name": "Alex Anzalone",          "team": "Detroit Lions",           "position": "LB",  "ig_handle": "alexanzalone"},
    {"name": "Carlton Davis",          "team": "Detroit Lions",           "position": "CB",  "ig_handle": "carltondavis3"},
    {"name": "Kerby Joseph",           "team": "Detroit Lions",           "position": "S",   "ig_handle": "kerbyjoseph"},

    # ── Green Bay Packers ─────────────────────────────────────────────────
    {"name": "Jordan Love",            "team": "Green Bay Packers",       "position": "QB",  "ig_handle": "jordan3love"},
    {"name": "Sean Clifford",          "team": "Green Bay Packers",       "position": "QB",  "ig_handle": "seanclifford14"},
    {"name": "Jayden Reed",            "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "jaydenreed11"},
    {"name": "Romeo Doubs",            "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "romeo.doubs"},
    {"name": "Christian Watson",       "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "christianwatson81"},
    {"name": "Dontayvion Wicks",       "team": "Green Bay Packers",       "position": "WR",  "ig_handle": "dontayvionwicks"},
    {"name": "Tucker Kraft",           "team": "Green Bay Packers",       "position": "TE",  "ig_handle": "tuckerkraft"},
    {"name": "Josh Jacobs",            "team": "Green Bay Packers",       "position": "RB",  "ig_handle": "iamjoshjacobs"},
    {"name": "Emanuel Wilson",         "team": "Green Bay Packers",       "position": "RB",  "ig_handle": "emanuelwilson"},
    {"name": "David Bakhtiari",        "team": "Green Bay Packers",       "position": "OT",  "ig_handle": "davidbakhtiari69"},
    {"name": "Rashan Gary",            "team": "Green Bay Packers",       "position": "LB",  "ig_handle": "rashaangary"},
    {"name": "Kenny Clark",            "team": "Green Bay Packers",       "position": "DT",  "ig_handle": "kennyclark97"},
    {"name": "Jaire Alexander",        "team": "Green Bay Packers",       "position": "CB",  "ig_handle": "jairealexander23"},
    {"name": "Xavier McKinney",        "team": "Green Bay Packers",       "position": "S",   "ig_handle": "xaviermckinney15"},
    {"name": "Quay Walker",            "team": "Green Bay Packers",       "position": "LB",  "ig_handle": "quaywalker10"},

    # ── Minnesota Vikings ─────────────────────────────────────────────────
    {"name": "Sam Darnold",            "team": "Minnesota Vikings",       "position": "QB",  "ig_handle": "samdarnold14"},
    {"name": "Nick Mullens",           "team": "Minnesota Vikings",       "position": "QB",  "ig_handle": "nickmullens"},
    {"name": "Justin Jefferson",       "team": "Minnesota Vikings",       "position": "WR",  "ig_handle": "justinjefferson"},
    {"name": "Jordan Addison",         "team": "Minnesota Vikings",       "position": "WR",  "ig_handle": "jordanaddison2"},
    {"name": "Jalen Nailor",           "team": "Minnesota Vikings",       "position": "WR",  "ig_handle": "jalennailor"},
    {"name": "T.J. Hockenson",         "team": "Minnesota Vikings",       "position": "TE",  "ig_handle": "tjhockenson"},
    {"name": "Aaron Jones",            "team": "Minnesota Vikings",       "position": "RB",  "ig_handle": "showtyme33_aj"},
    {"name": "Ty Chandler",            "team": "Minnesota Vikings",       "position": "RB",  "ig_handle": "tychandler"},
    {"name": "Christian Darrisaw",     "team": "Minnesota Vikings",       "position": "OT",  "ig_handle": "christiandarrisaw"},
    {"name": "Jonathan Greenard",      "team": "Minnesota Vikings",       "position": "DE",  "ig_handle": "jgreenard"},
    {"name": "Harrison Smith",         "team": "Minnesota Vikings",       "position": "S",   "ig_handle": "harrisonsmith22"},
    {"name": "Byron Murphy",           "team": "Minnesota Vikings",       "position": "CB",  "ig_handle": "byronmurphy"},
    {"name": "Andrew Van Ginkel",      "team": "Minnesota Vikings",       "position": "LB",  "ig_handle": "andrewvanginkel"},
    {"name": "Brian Asamoah II",       "team": "Minnesota Vikings",       "position": "LB",  "ig_handle": "brianasamoah"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC SOUTH
    # ════════════════════════════════════════════════════════════════════════

    # ── Atlanta Falcons ───────────────────────────────────────────────────
    {"name": "Kirk Cousins",           "team": "Atlanta Falcons",         "position": "QB",  "ig_handle": "kirkcousins8"},
    {"name": "Michael Penix Jr.",      "team": "Atlanta Falcons",         "position": "QB",  "ig_handle": "michaelpenixjr"},
    {"name": "Drake London",           "team": "Atlanta Falcons",         "position": "WR",  "ig_handle": "drakelo44"},
    {"name": "Darnell Mooney",         "team": "Atlanta Falcons",         "position": "WR",  "ig_handle": "darnellmooney11"},
    {"name": "Rondale Moore",          "team": "Atlanta Falcons",         "position": "WR",  "ig_handle": "rondalemore"},
    {"name": "Kyle Pitts",             "team": "Atlanta Falcons",         "position": "TE",  "ig_handle": "kylepitts88"},
    {"name": "Bijan Robinson",         "team": "Atlanta Falcons",         "position": "RB",  "ig_handle": "bijan4robinson"},
    {"name": "Tyler Allgeier",         "team": "Atlanta Falcons",         "position": "RB",  "ig_handle": "tylerallgeier"},
    {"name": "Jake Matthews",          "team": "Atlanta Falcons",         "position": "OT",  "ig_handle": "jakematthews"},
    {"name": "Matthew Judon",          "team": "Atlanta Falcons",         "position": "LB",  "ig_handle": "mattjudon"},
    {"name": "Grady Jarrett",          "team": "Atlanta Falcons",         "position": "DT",  "ig_handle": "gradyjarrett"},
    {"name": "A.J. Terrell",           "team": "Atlanta Falcons",         "position": "CB",  "ig_handle": "aj_terrell8"},
    {"name": "Jessie Bates III",       "team": "Atlanta Falcons",         "position": "S",   "ig_handle": "jessiebates"},
    {"name": "Kaden Elliss",           "team": "Atlanta Falcons",         "position": "LB",  "ig_handle": "kadenelliss"},

    # ── Carolina Panthers ─────────────────────────────────────────────────
    {"name": "Bryce Young",            "team": "Carolina Panthers",       "position": "QB",  "ig_handle": "bryceyoung"},
    {"name": "Andy Dalton",            "team": "Carolina Panthers",       "position": "QB",  "ig_handle": "andydalton14"},
    {"name": "Adam Thielen",           "team": "Carolina Panthers",       "position": "WR",  "ig_handle": "adamthielen19"},
    {"name": "Diontae Johnson",        "team": "Carolina Panthers",       "position": "WR",  "ig_handle": "diontaejohnson18"},
    {"name": "Jonathan Mingo",         "team": "Carolina Panthers",       "position": "WR",  "ig_handle": "jonathanmingo"},
    {"name": "Hayden Hurst",           "team": "Carolina Panthers",       "position": "TE",  "ig_handle": "haydenhurst"},
    {"name": "Chuba Hubbard",          "team": "Carolina Panthers",       "position": "RB",  "ig_handle": "chubahubbard"},
    {"name": "Miles Sanders",          "team": "Carolina Panthers",       "position": "RB",  "ig_handle": "milesdontmiss"},
    {"name": "Ikem Ekwonu",            "team": "Carolina Panthers",       "position": "OT",  "ig_handle": "ikemekwonu"},
    {"name": "Derrick Brown",          "team": "Carolina Panthers",       "position": "DT",  "ig_handle": "derrickbrown5"},
    {"name": "Jaycee Horn",            "team": "Carolina Panthers",       "position": "CB",  "ig_handle": "jayceehorn"},
    {"name": "Xavier Woods",           "team": "Carolina Panthers",       "position": "S",   "ig_handle": "xavierwoods25"},
    {"name": "Shaq Thompson",          "team": "Carolina Panthers",       "position": "LB",  "ig_handle": "shaqthompson7"},

    # ── New Orleans Saints ────────────────────────────────────────────────
    {"name": "Derek Carr",             "team": "New Orleans Saints",      "position": "QB",  "ig_handle": "derekcarrqb4"},
    {"name": "Jameis Winston",         "team": "New Orleans Saints",      "position": "QB",  "ig_handle": "jameis3winston"},
    {"name": "Chris Olave",            "team": "New Orleans Saints",      "position": "WR",  "ig_handle": "chrisolave_"},
    {"name": "Rashid Shaheed",         "team": "New Orleans Saints",      "position": "WR",  "ig_handle": "rashidshaheed"},
    {"name": "A.T. Perry",             "team": "New Orleans Saints",      "position": "WR",  "ig_handle": "atperry7"},
    {"name": "Juwan Johnson",          "team": "New Orleans Saints",      "position": "TE",  "ig_handle": "juwanjohnson"},
    {"name": "Foster Moreau",          "team": "New Orleans Saints",      "position": "TE",  "ig_handle": "fostermoreau"},
    {"name": "Alvin Kamara",           "team": "New Orleans Saints",      "position": "RB",  "ig_handle": "alvinkamara41"},
    {"name": "Kendre Miller",          "team": "New Orleans Saints",      "position": "RB",  "ig_handle": "kendremiller"},
    {"name": "Trevor Penning",         "team": "New Orleans Saints",      "position": "OT",  "ig_handle": "trevorpenning"},
    {"name": "Cameron Jordan",         "team": "New Orleans Saints",      "position": "DE",  "ig_handle": "camjordan94"},
    {"name": "Marshon Lattimore",      "team": "New Orleans Saints",      "position": "CB",  "ig_handle": "marshawnlattimore"},
    {"name": "Tyrann Mathieu",         "team": "New Orleans Saints",      "position": "S",   "ig_handle": "tyrannmathieu32"},
    {"name": "Pete Werner",            "team": "New Orleans Saints",      "position": "LB",  "ig_handle": "petewerner"},
    {"name": "Bryan Bresee",           "team": "New Orleans Saints",      "position": "DT",  "ig_handle": "bryanbresee"},

    # ── Tampa Bay Buccaneers ──────────────────────────────────────────────
    {"name": "Baker Mayfield",         "team": "Tampa Bay Buccaneers",    "position": "QB",  "ig_handle": "bakermayfield"},
    {"name": "Kyle Trask",             "team": "Tampa Bay Buccaneers",    "position": "QB",  "ig_handle": "kyletrask"},
    {"name": "Mike Evans",             "team": "Tampa Bay Buccaneers",    "position": "WR",  "ig_handle": "mr_evans13"},
    {"name": "Chris Godwin",           "team": "Tampa Bay Buccaneers",    "position": "WR",  "ig_handle": "cgodwin14"},
    {"name": "Trey Palmer",            "team": "Tampa Bay Buccaneers",    "position": "WR",  "ig_handle": "treypalmer"},
    {"name": "Cade Otton",             "team": "Tampa Bay Buccaneers",    "position": "TE",  "ig_handle": "cadeotton"},
    {"name": "Rachaad White",          "team": "Tampa Bay Buccaneers",    "position": "RB",  "ig_handle": "rachaadwhite"},
    {"name": "Bucky Irving",           "team": "Tampa Bay Buccaneers",    "position": "RB",  "ig_handle": "buckyirving"},
    {"name": "Tristan Wirfs",          "team": "Tampa Bay Buccaneers",    "position": "OT",  "ig_handle": "tristanwirfs"},
    {"name": "Vita Vea",               "team": "Tampa Bay Buccaneers",    "position": "DT",  "ig_handle": "vitavea75"},
    {"name": "Calijah Kancey",         "team": "Tampa Bay Buccaneers",    "position": "DT",  "ig_handle": "calijakancey"},
    {"name": "Lavonte David",          "team": "Tampa Bay Buccaneers",    "position": "LB",  "ig_handle": "lavontedavid54"},
    {"name": "Antoine Winfield Jr.",   "team": "Tampa Bay Buccaneers",    "position": "S",   "ig_handle": "antoinewingfield"},
    {"name": "Zyon McCollum",          "team": "Tampa Bay Buccaneers",    "position": "CB",  "ig_handle": "zyonmccollum"},
    {"name": "Keeanu Benton",          "team": "Tampa Bay Buccaneers",    "position": "DT",  "ig_handle": "keeanu_benton"},

    # ════════════════════════════════════════════════════════════════════════
    # NFC WEST
    # ════════════════════════════════════════════════════════════════════════

    # ── Arizona Cardinals ─────────────────────────────────────────────────
    {"name": "Kyler Murray",           "team": "Arizona Cardinals",       "position": "QB",  "ig_handle": "kyler1murray"},
    {"name": "Clayton Tune",           "team": "Arizona Cardinals",       "position": "QB",  "ig_handle": "claytontune"},
    {"name": "Marvin Harrison Jr.",    "team": "Arizona Cardinals",       "position": "WR",  "ig_handle": "marvharrisonjr"},
    {"name": "Greg Dortch",            "team": "Arizona Cardinals",       "position": "WR",  "ig_handle": "greg.dortch"},
    {"name": "Michael Wilson",         "team": "Arizona Cardinals",       "position": "WR",  "ig_handle": "michaelwilson3"},
    {"name": "Trey McBride",           "team": "Arizona Cardinals",       "position": "TE",  "ig_handle": "treymcbride85"},
    {"name": "James Conner",           "team": "Arizona Cardinals",       "position": "RB",  "ig_handle": "realcontact30"},
    {"name": "Emari Demercado",        "team": "Arizona Cardinals",       "position": "RB",  "ig_handle": "emaridemercado"},
    {"name": "Paris Johnson Jr.",      "team": "Arizona Cardinals",       "position": "OT",  "ig_handle": "parisjohnsonjr"},
    {"name": "Budda Baker",            "team": "Arizona Cardinals",       "position": "S",   "ig_handle": "buddabaker32"},
    {"name": "Zaven Collins",          "team": "Arizona Cardinals",       "position": "LB",  "ig_handle": "zavencollins"},
    {"name": "Dennis Gardeck",         "team": "Arizona Cardinals",       "position": "LB",  "ig_handle": "dennisgardeck"},
    {"name": "Sean Murphy-Bunting",    "team": "Arizona Cardinals",       "position": "CB",  "ig_handle": "seanmurphybunting"},
    {"name": "Kei'Trel Clark",         "team": "Arizona Cardinals",       "position": "CB",  "ig_handle": "keitrelclark"},

    # ── Los Angeles Rams ──────────────────────────────────────────────────
    {"name": "Matthew Stafford",       "team": "Los Angeles Rams",        "position": "QB",  "ig_handle": "matthewstafford9"},
    {"name": "Jimmy Garoppolo",        "team": "Los Angeles Rams",        "position": "QB",  "ig_handle": "jimmygaroppolo"},
    {"name": "Cooper Kupp",            "team": "Los Angeles Rams",        "position": "WR",  "ig_handle": "cooperkupp"},
    {"name": "Puka Nacua",             "team": "Los Angeles Rams",        "position": "WR",  "ig_handle": "pukanacua17"},
    {"name": "Demarcus Robinson",      "team": "Los Angeles Rams",        "position": "WR",  "ig_handle": "d_rob"},
    {"name": "Tyler Higbee",           "team": "Los Angeles Rams",        "position": "TE",  "ig_handle": "tylerhigbee89"},
    {"name": "Colby Parkinson",        "team": "Los Angeles Rams",        "position": "TE",  "ig_handle": "colbyparkinson"},
    {"name": "Kyren Williams",         "team": "Los Angeles Rams",        "position": "RB",  "ig_handle": "kyrenwilliams"},
    {"name": "Blake Corum",            "team": "Los Angeles Rams",        "position": "RB",  "ig_handle": "blakecorum"},
    {"name": "Rob Havenstein",         "team": "Los Angeles Rams",        "position": "OT",  "ig_handle": "robhavenstein"},
    {"name": "Jared Verse",            "team": "Los Angeles Rams",        "position": "DE",  "ig_handle": "jaredverse"},
    {"name": "Kobie Turner",           "team": "Los Angeles Rams",        "position": "DT",  "ig_handle": "kobieturner"},
    {"name": "Ernest Jones IV",        "team": "Los Angeles Rams",        "position": "LB",  "ig_handle": "ernestjones"},
    {"name": "Ahkello Witherspoon",    "team": "Los Angeles Rams",        "position": "CB",  "ig_handle": "ahkellowitherspoon"},
    {"name": "Jordan Fuller",          "team": "Los Angeles Rams",        "position": "S",   "ig_handle": "jordanfuller"},

    # ── San Francisco 49ers ───────────────────────────────────────────────
    {"name": "Brock Purdy",            "team": "San Francisco 49ers",     "position": "QB",  "ig_handle": "brockpurdy13"},
    {"name": "Brandon Allen",          "team": "San Francisco 49ers",     "position": "QB",  "ig_handle": "brandonallen10"},
    {"name": "Deebo Samuel",           "team": "San Francisco 49ers",     "position": "WR",  "ig_handle": "debo"},
    {"name": "Brandon Aiyuk",          "team": "San Francisco 49ers",     "position": "WR",  "ig_handle": "_brandonaiyuk"},
    {"name": "Jauan Jennings",         "team": "San Francisco 49ers",     "position": "WR",  "ig_handle": "jauan17"},
    {"name": "George Kittle",          "team": "San Francisco 49ers",     "position": "TE",  "ig_handle": "gkittle46"},
    {"name": "Cameron Latu",           "team": "San Francisco 49ers",     "position": "TE",  "ig_handle": "cameronlatu"},
    {"name": "Christian McCaffrey",    "team": "San Francisco 49ers",     "position": "RB",  "ig_handle": "christianmccaffrey"},
    {"name": "Jordan Mason",           "team": "San Francisco 49ers",     "position": "RB",  "ig_handle": "jordanmason24"},
    {"name": "Trent Williams",         "team": "San Francisco 49ers",     "position": "OT",  "ig_handle": "trent"},
    {"name": "Nick Bosa",              "team": "San Francisco 49ers",     "position": "DE",  "ig_handle": "nbsmallerbear"},
    {"name": "Fred Warner",            "team": "San Francisco 49ers",     "position": "LB",  "ig_handle": "fredwarner"},
    {"name": "Charvarius Ward",        "team": "San Francisco 49ers",     "position": "CB",  "ig_handle": "manhuntward21"},
    {"name": "Talanoa Hufanga",        "team": "San Francisco 49ers",     "position": "S",   "ig_handle": "talanoahufanga"},

    # ── Seattle Seahawks ──────────────────────────────────────────────────
    {"name": "Geno Smith",             "team": "Seattle Seahawks",        "position": "QB",  "ig_handle": "genosmith7"},
    {"name": "Sam Howell",             "team": "Seattle Seahawks",        "position": "QB",  "ig_handle": "samhowell14"},
    {"name": "DK Metcalf",             "team": "Seattle Seahawks",        "position": "WR",  "ig_handle": "dkmetcalf14"},
    {"name": "Tyler Lockett",          "team": "Seattle Seahawks",        "position": "WR",  "ig_handle": "tlockett16"},
    {"name": "Jaxon Smith-Njigba",     "team": "Seattle Seahawks",        "position": "WR",  "ig_handle": "jaxonsmithnjigba"},
    {"name": "Noah Fant",              "team": "Seattle Seahawks",        "position": "TE",  "ig_handle": "noahfant"},
    {"name": "Kenneth Walker III",     "team": "Seattle Seahawks",        "position": "RB",  "ig_handle": "kennywalker22"},
    {"name": "Zach Charbonnet",        "team": "Seattle Seahawks",        "position": "RB",  "ig_handle": "zachcharb"},
    {"name": "Charles Cross",          "team": "Seattle Seahawks",        "position": "OT",  "ig_handle": "charlescross"},
    {"name": "Leonard Williams",       "team": "Seattle Seahawks",        "position": "DT",  "ig_handle": "leonardwilliams99"},
    {"name": "Boye Mafe",              "team": "Seattle Seahawks",        "position": "DE",  "ig_handle": "boyemafe"},
    {"name": "Uchenna Nwosu",          "team": "Seattle Seahawks",        "position": "LB",  "ig_handle": "uchennanwosu"},
    {"name": "Tariq Woolen",           "team": "Seattle Seahawks",        "position": "CB",  "ig_handle": "tariqwoolen"},
    {"name": "Quandre Diggs",          "team": "Seattle Seahawks",        "position": "S",   "ig_handle": "quandrediggs"},
]


def seed_players():
    """Populate the players table. Safe to run multiple times (upsert)."""
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
