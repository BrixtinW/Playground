import os
from art import *
from utils.display_utils import clear_screen, center
from game.game_initializer import initialize_game
from game.game_loop import run_game_loop
from worldMap import displayMap


def main_menu():
    """Display and handle the main menu."""
    while True:
        clear_screen()
        display_menu_header()
        display_menu_options()
        
        choice = input('Enter your choice: ')
        clear_screen()
        
        if handle_menu_choice(choice):
            break

def display_menu_header():
    """Display the menu header."""
    width = os.get_terminal_size().columns
    title = "  GAME MENU  "
    title_line = "=" * ((width - len(title)) // 2) + title + "=" * ((width - len(title)) // 2)
    print(title_line)
    
    # Display ASCII art (img2 needs to be defined or imported)
    terminal_width = os.get_terminal_size().columns
    for line in img2:
        spaces = (terminal_width - len(line)) // 2
        halfway = " " * spaces
        line = halfway.join(line)
        print(line)

def display_menu_options():
    """Display the menu options."""
    width = os.get_terminal_size().columns
    print("-" * width)
    print("1. Start Game")
    print("2. Tutorial")
    print("3. Settings")
    print("4. Quit")
    print("-" * width)

def handle_menu_choice(choice):
    """Handle the menu choice selection."""
    if choice == "1":
        start_game()
    elif choice == "2":
        show_tutorial()
    elif choice == "3":
        show_settings_menu()
    elif choice == "4":
        print("Thanks for playing!\n\n")
        return True
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
    return False

def start_game():
    """Start a new game."""
    kingdoms = initialize_game()
    world_map = displayMap(kingdoms)
    run_game_loop(kingdoms, world_map)

def show_tutorial():
    """Show the tutorial."""
    print("Tutorial not yet implemented...")
    input("Press Enter to continue...")

def show_settings_menu():
    """Show the settings menu."""
    while True:
        print("SETTINGS MENU")
        print("1. Sound")
        print("2. Graphics")
        print("3. Controls")
        print("4. Back")
        
        choice = input("Enter your choice: ")
        clear_screen()
        
        if handle_settings_choice(choice):
            break

def handle_settings_choice(choice):
    """Handle the settings menu choice."""
    if choice == "1":
        show_sound_menu()
    elif choice == "2":
        show_graphics_menu()
    elif choice == "3":
        show_controls_menu()
    elif choice == "4":
        return True
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
    return False

def show_sound_menu():
    """Show the sound settings menu."""
    print("SOUND MENU")
    input("Press Enter to continue...")

def show_graphics_menu():
    """Show the graphics settings menu."""
    print("GRAPHICS MENU")
    input("Press Enter to continue...")

def show_controls_menu():
    """Show the controls settings menu."""
    print("CONTROLS MENU")
    input("Press Enter to continue...")

# ------------------------------------------------------------------------------------

if __name__ == "__main__":
    main_menu()