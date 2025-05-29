from config.game_constants import KINGDOMS
from models.kingdom import Kingdom
from utils.display_utils import clear_screen

def initialize_game():
    """Initialize a new game by getting player count and kingdom selections."""
    clear_screen()
    print("Starting new game...")
    num_players = int(input("Number of Players: "))
    
    print(f"Select {num_players} options:")
    selected_kingdoms = get_player_kingdom_selections(num_players)
    
    print("Selected options:")
    for player, kingdom in selected_kingdoms.items():
        print(f"Player {player}: {kingdom}")
    input("Press Enter to continue...")
    
    return create_kingdom_instances(selected_kingdoms)

def get_player_kingdom_selections(num_players):
    """Get kingdom selections from each player."""
    selected_kingdoms = {}
    available_kingdoms = list(KINGDOMS.keys())
    
    while len(selected_kingdoms) < num_players:
        current_player = len(selected_kingdoms) + 1
        display_available_kingdoms(available_kingdoms)
        
        choice = input(f"Player {current_player}, select an option: ")
        if validate_kingdom_choice(choice, available_kingdoms):
            kingdom_name = available_kingdoms[int(choice) - 1]
            selected_kingdoms[current_player] = kingdom_name
            available_kingdoms.remove(kingdom_name)
            clear_screen()
            print(f"{kingdom_name} selected!")
        else:
            clear_screen()
            print("Invalid choice. Try again.")
            
    return selected_kingdoms

def display_available_kingdoms(available_kingdoms):
    """Display available kingdoms for selection."""
    for i, kingdom in enumerate(available_kingdoms, 1):
        print(f"{i}. {kingdom}")

def validate_kingdom_choice(choice, available_kingdoms):
    """Validate if the kingdom choice is valid."""
    return choice.isdigit() and int(choice) in range(1, len(available_kingdoms) + 1)

def create_kingdom_instances(selected_kingdoms):
    """Create Kingdom instances from selected kingdoms."""
    kingdom_instances = {}
    for player_num, kingdom_name in selected_kingdoms.items():
        kingdom_data = KINGDOMS[kingdom_name]
        kingdom_instances[kingdom_name] = Kingdom(
            player_num,
            kingdom_name,
            kingdom_data["capital_name"],
            kingdom_data["ruler"],
            kingdom_data["advisor"],
            kingdom_data["warrior"],
            kingdom_data["color"]
        )
    return kingdom_instances 