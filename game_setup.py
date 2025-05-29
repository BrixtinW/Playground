import os
from turns import play_game

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_game():
    clear_screen()
    print("Starting new game...")
    numPlayers = int(input("Number of Players: "))
    # Define list of options
    options = ["Hyrule", "Icarus", "Koopa Kingdom", "Ylisse",
               "Mushroom Kingdom", "D.U.S.T.", "Gaur", "Dreamland"]

    print("Select {} options:".format(str(numPlayers)))

    selected_options = {}
    while len(selected_options) < numPlayers:
        current_player = len(selected_options) + 1
        for i, option in enumerate(options):
            if option not in selected_options.values():
                print("{}. {}".format(i+1, option))
        choice = input("Player " + str(current_player) + ", select an option: ")
        if choice.isdigit() and int(choice) in range(1, len(options)+1):
            choice_idx = int(choice) - 1
            if options[choice_idx] not in selected_options.values():
                selected_options[current_player] = options[choice_idx]
                current_player += 1
                clear_screen()
                print("{} selected!".format(options[choice_idx]))
            else:
                clear_screen()
                print("Option already selected!")
        else:
            clear_screen()
            print("Invalid choice. Try again.")


    print("Selected options:")
    for player, option in selected_options.items():
        print("Player {}: {}".format(player, option))
    input("Press Enter to continue...")

    play_game(selected_options)

