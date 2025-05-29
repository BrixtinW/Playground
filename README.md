# Kingdom Battle Game

A turn-based strategy game where players control kingdoms and battle for supremacy.

## Setup

1. Make sure you have Python 3.7+ installed
2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Running the Game

From the project root directory:
```bash
# Make sure your virtual environment is activated, then:
python3 game.py
```

## Game Controls

- Use number keys (1-4) to select menu options
- Follow on-screen prompts for gameplay actions
- Use 'x' to go back or cancel actions

## Features

- Multiple kingdoms with unique rulers and advisors
- Turn-based strategy gameplay
- Resource management
- Army building and combat
- Territory expansion

## Project Structure

```
.
├── config/             # Game configuration and constants
│   ├── __init__.py
│   └── game_constants.py
├── utils/             # Utility functions
│   ├── __init__.py
│   └── display_utils.py
├── game/              # Core game logic
│   ├── __init__.py
│   ├── game_initializer.py
│   └── game_loop.py
├── models/            # Game models
│   ├── __init__.py
│   ├── battalion.py
│   ├── kingdom.py
│   └── land.py
├── game.py           # Main game file
├── requirements.txt   # Dependencies
└── README.md         # This file
```

## Troubleshooting

If you encounter import errors:
1. Make sure you're in the project root directory
2. Ensure your virtual environment is activated
3. Verify all dependencies are installed: `pip3 list`
4. Check that all `__init__.py` files are present in each directory
5. Try running with the full Python path: `/usr/bin/python3 game.py` 