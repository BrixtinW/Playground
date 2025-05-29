from utils.display_utils import display_transition_page, display_game_header

def run_game_loop(kingdoms, world_map):
    """Run the main game loop."""
    turn = 0
    game_over = False
    
    while not game_over:
        turn += 1
        game_over = process_turn(turn, kingdoms, world_map)

def process_turn(turn, kingdoms, world_map):
    """Process a single game turn for all kingdoms."""
    for kingdom_name, kingdom in kingdoms.items():
        if not kingdom.defeated:
            display_transition_page(kingdom_name)
            if handle_kingdom_turn(turn, kingdoms, kingdom, world_map):
                return True
    return False

def handle_kingdom_turn(turn, kingdoms, kingdom, world_map):
    """Handle a single kingdom's turn."""
    kingdom.updateVariables()
    display_game_header(kingdom.name, turn, kingdom)
    kingdom.printCities(turn)

    if turn != 1:
        kingdom.updateExcel()

    while True:
        option = input("Choose an option: ").strip()
        
        if option == "1":
            kingdom.buy(input("Select what you would like to buy:\n"))
        elif option == "2":
            request = input("please input with the format [location] [character] [direction]\n(remember A for all, M for multiple, and x to go back) \nwho would you like to move:\n")
            kingdom.moveRequest(world_map, request, turn, kingdoms)
        elif option == "4":
            return True
        elif option == "3":
            process_end_turn(kingdom)
            break

        display_game_header(kingdom.name, turn, kingdom)
        kingdom.printCities(turn)
        kingdom.updateExcel()
    
    return False

def process_end_turn(kingdom):
    """Process end of turn actions for a kingdom."""
    for i in range(len(kingdom.lands)):
        if kingdom.lands[i].numAvailablePeasants > 0:
            kingdom.buy(f"{i+1} {kingdom.lands[i].numAvailablePeasants} g") 