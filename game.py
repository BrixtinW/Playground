import os
from art import *
from game_setup import run_game


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    clear_screen()
    width = os.get_terminal_size().columns
    title = "  GAME MENU  "
    title_line = "=" * ((width - len(title)) // 2) + title + "=" * ((width - len(title)) // 2)
    print(title_line)

    # this following line puts the text at the bottom of the screen, and I can add it later when I figure out how to add ASCII art to the space above it. 
    # Get the width of the terminal
    terminal_width = os.get_terminal_size().columns

    for line in img2:
         # Calculate the number of spaces needed to center the text
        spaces = (terminal_width - len(line)) // 2

        halfway = " " * spaces
        line = halfway.join(line)
         # Print the text with the appropriate number of spaces before it
        print(line)

    print("-" * width)
    print("1. Start Game")
    print("2. Tutorial")
    print("3. Settings")
    print("4. Quit")
    print("-" * width)
    choice = input('Enter your choice: ')
    clear_screen()

    if choice == "1":
        run_game()
    elif choice == "2":
        Tutorial()
    elif choice == "3":
        settings_menu()
    elif choice == "4":
        print("Thanks for playing!\n\n")
        return
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        clear_screen()
        main_menu()

def Tutorial():
    print("Tutorial not yet implemented...")
    # load game code goes here
    input("Press Enter to continue...")
    clear_screen()
    main_menu()

def settings_menu():
    print("SETTINGS MENU")
    print("1. Sound")
    print("2. Graphics")
    print("3. Controls")
    print("4. Back")

    choice = input("Enter your choice: ")
    clear_screen()

    if choice == "1":
        sound_menu()
    elif choice == "2":
        graphics_menu()
    elif choice == "3":
        controls_menu()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        clear_screen()
        settings_menu()

def sound_menu():
    print("SOUND MENU")
    input("Press Enter to continue...")
    clear_screen()
    settings_menu()

def graphics_menu():
    print("GRAPHICS MENU")
    input("Press Enter to continue...")
    clear_screen()
    settings_menu()

def controls_menu():
    print("CONTROLS MENU")
    input("Press Enter to continue...")
    clear_screen()
    settings_menu()

# ------------------------------------------------------------------------------------

main_menu()