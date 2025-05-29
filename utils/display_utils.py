import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def center(text, characters=" "):
    """Center text in the terminal with optional padding characters."""
    width = os.get_terminal_size().columns
    centered_text = characters * ((width - len(text)) // 2) + text + characters * ((width - len(text)) // 2)
    print(centered_text)

def display_transition_page(kingdom_name):
    """Display a transition page for a kingdom's turn."""
    clear_screen()
    for _ in range(7):
        center(" ", " ")
    center("-", "-")
    center(" ", " ")
    center("=", "=")
    center(" ", " ")
    center("-", "-")
    center(f"|    {kingdom_name}'s turn    |", "|")
    center("-", "-")
    center(" ", " ")
    center("=", "=")
    center(" ", " ")
    center("-", "-")
    for _ in range(7):
        center(" ", " ")
    input()

def display_game_header(kingdom_name, turn, kingdom):
    """Display the game header with kingdom information and market prices."""
    clear_screen()
    center("-", "-")
    center((f"  {kingdom_name}'s Turn  "), "=")
    center(" Options ------------------------------------- Market ", "-")
    center("1: Buy                           |   Peasant:  $3    Battalion: $7 ")
    center("    2: Move                          |   Merchant: $10   Training:  (level)")
    center("3: End Turn                      |   Gold:     $0    Housing:   $10")
    center("4: Quit Game                     |   Conscript:$5    Health:    $10")
    center("-", "-")
    center(f"Turn: {turn}    Gold: ${kingdom.gold}    Production: {kingdom.production}    Number of Cities: {kingdom.numCities}")
    center(f"Leader: {kingdom.ruler.name} {kingdom.ruler.display_health()}   Advisor: {kingdom.advisor.name} {kingdom.advisor.display_health()}   Warrior: {kingdom.warrior}")
    center("-", "-") 