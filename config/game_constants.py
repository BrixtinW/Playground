KINGDOMS = {
    "Hyrule": {
        "ruler": "Ganondorf",
        "advisor": "Zelda",
        "warrior": "Link",
        "capital_name": "Temple",
        "color": '98FB98'
    },
    "Icarus": {
        "ruler": "Palutena",
        "advisor": "Ness",
        "warrior": "Wii Fit Trainer",
        "capital_name": "Palutena's Temple",
        "color": 'FFFF00'
    },
    "Koopa Kingdom": {
        "ruler": "Bowser",
        "advisor": "Bowser Jr.",
        "warrior": "Mr. Game & Watch",
        "capital_name": "Luigi's Mansion",
        "color": '9370DB'
    },
    "Ylisse": {
        "ruler": "Lucina",
        "advisor": "Ike",
        "warrior": "Marth",
        "capital_name": "Kalos Pokemon League",
        "color": 'ADD8E6'
    },
    "Mushroom Kingdom": {
        "ruler": "Peach",
        "advisor": "Rosalina",
        "warrior": "Mario",
        "capital_name": "Delfino Plaza",
        "color": 'FF0000'
    },
    "D.U.S.T.": {
        "ruler": "Zero Suit Samus",
        "advisor": "Samus",
        "warrior": "R.O.B.",
        "capital_name": "Mario Galaxy",
        "color": 'FFA500'
    },
    "Gaur": {
        "ruler": "Lucario",
        "advisor": "Greninja",
        "warrior": "Sonic",
        "capital_name": "Gaur Plain",
        "color": 'D2B48C'
    },
    "Dreamland": {
        "ruler": "King Dedede",
        "advisor": "Kirby",
        "warrior": "Villager",
        "capital_name": "The Great Cave Offensive",
        "color": 'FFC0CB'
    }
}

CHARACTER_ABBREVIATIONS = {
    'g': "Ganondorf",
    'z': "Zelda",
    'pt': "Palutena",
    'n': "Ness",
    'b': "Bowser",
    'bj': "Bowser Jr.",
    'l': "Lucina",
    'i': "Ike",
    'p': "Peach",
    'r': "Rosalina",
    'zs': "Zero Suit Samus",
    's': "Samus",
    'lc': "Lucario",
    'gr': "Greninja",
    'kd': "King Dedede",
    'k': "Kirby"
}

MARKET_PRICES = {
    "p": 3,  # Peasant
    "g": 0,  # Gold
    "b": 7,  # Battalion
    "m": 7,  # Merchant
    "t": 1,  # Training
    "c": 5,  # Conscript
    "h": 10, # Housing
    "hp": 10 # Health Point
}

PURCHASE_WAIT_TIMES = {
    "p": 1,  # Peasant
    "g": 1,  # Gold
    "b": 1,  # Battalion
    "m": 2,  # Merchant
    "t": 1,  # Training
    "c": 0,  # Conscript
    "h": 2,  # Housing
    "hp": 0  # Health Point
}

MOVEMENT_DIRECTIONS = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1),
    'u': (-1, 0),
    'r': (0, 1),
    'd': (1, 0),
    'l': (0, -1)
}

VALID_MOVE_FORMATS = ['up', 'right', 'down', 'left', 'u', 'r', 'd', 'l']

# Excel map configuration
EXCEL_CONFIG = {
    'column_width': 20,
    'row_height': 80,
    'start_col': 8,
    'start_row': 8,
    'end_col': 18,
    'end_row': 15,
    'default_land_color': 'D3D3D3'
}

# Initial kingdom stats
INITIAL_KINGDOM_STATS = {
    'gold': 21,
    'defeated': False
} 