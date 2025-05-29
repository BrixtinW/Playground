from kingdoms import *
# import os
from worldMap import *
# import sys

width = os.get_terminal_size().columns

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def center(text, characters=" "):
#     width = os.get_terminal_size().columns
#     centered_text = characters * ((width - len(text)) // 2) + text + characters * ((width - len(text)) // 2)
#     print(centered_text)

def transitionPage(currentKingdom):
    clear_screen()
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center("-","-")
    center(" "," ")
    center("=","=")
    center(" "," ")
    center("-","-")
    center(f"|    {currentKingdom}'s turn    |","|")
    center("-","-")
    center(" "," ")
    center("=","=")
    center(" "," ")
    center("-","-")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    center(" "," ")
    input()

def header(currentKingdom, turn, kingdoms):
    clear_screen()
    center("-","-")
    center((f"  " + currentKingdom + "'s Turn  "), "=")
    center(" Options ------------------------------------- Market ", "-")
    center("1: Buy                           |   Peasant:  $3    Battalion: $7 ")
    center("    2: Move                          |   Merchant: $10   Training:  (level)")
    center("3: End Turn                      |   Gold:     $0    Housing:   $10")
    center("4: Quit Game                     |   Conscript:$5    Health:    $10")
    center("-","-")
    center(f"Turn: " + str(turn) + "    Gold: $" + str(kingdoms[currentKingdom].gold) +"    Production: " + str(kingdoms[currentKingdom].production) + "    Number of Cities: " + str(kingdoms[currentKingdom].numCities))
    center(f"Leader: " + kingdoms[currentKingdom].ruler.name + " " + kingdoms[currentKingdom].ruler.display_health() + "   Advisor: " + kingdoms[currentKingdom].advisor.name + " " + kingdoms[currentKingdom].advisor.display_health() + "   Warrior: " + kingdoms[currentKingdom].warrior)
    center("-","-")

def defineKingdoms(selected_options):
    print(selected_options)

    kingdoms = {}

    for player in selected_options.keys():
        if selected_options[player] == "Hyrule":
            kingdomName = "Hyrule"
            ruler = "Ganondorf"
            advisor = "Zelda"
            warrior = "Link"
            capitalName = "Temple"
            color = '98FB98'
        elif selected_options[player] == "Icarus":
            kingdomName = "Icarus"
            ruler = "Palutena"
            advisor = "Ness"
            warrior = "Wii Fit Trainer"
            capitalName = "Palutena's Temple"
            color = 'FFFF00'
        elif selected_options[player] == "Koopa Kingdom":
            kingdomName = "Koopa Kingdom"
            ruler = "Bowser"
            advisor = "Bowser Jr."
            warrior = "Mr. Game & Watch"
            capitalName = "Luigi's Mansion"
            color = '9370DB'
        elif selected_options[player] == "Ylisse":
            kingdomName = "Ylisse"
            ruler = "Lucina"
            advisor = "Ike"
            warrior = "Marth"
            capitalName = "Kalos Pokemon League"
            color = 'ADD8E6'
        elif selected_options[player] == "Mushroom Kingdom":
            kingdomName = "Mushroom Kingdom"
            ruler = "Peach"
            advisor = "Rosalina"
            warrior = "Mario"
            capitalName = "Delfino Plaza"
            color = 'FF0000'
        elif selected_options[player] == "D.U.S.T.":
            kingdomName = "D.U.S.T."
            ruler = "Zero Suit Samus"
            advisor = "Samus"
            warrior = "R.O.B."
            capitalName = "Mario Galaxy"
            color = 'FFA500'
        elif selected_options[player] == "Gaur":
            kingdomName = "Gaur"
            ruler = "Lucario"
            advisor = "Greninja"
            warrior = "Sonic"
            capitalName = "Gaur Plain"
            color = 'D2B48C'
        elif selected_options[player] == "Dreamland":
            kingdomName = "Dreamland"
            ruler = "King Dedede"
            advisor = "Kirby"
            warrior = "Villager"
            capitalName = "The Great Cave Offensive"
            color = 'FFC0CB'
        

        kingdoms[kingdomName] = Kingdom(player, kingdomName, capitalName, ruler, advisor, warrior, color)
    return kingdoms
    


def takeTurn(turn, kingdoms, currentKingdom, gameOver, world_map):
    kingdoms[currentKingdom.name].updateVariables()
    # sys.stdout.write('\033[1m')  # make the header bold
    header(currentKingdom.name, turn, kingdoms)
    # sys.stdout.write('\033[0m')  # reset to normal font
    currentKingdom.printCities(turn)

    if turn != 1:
    # the first time this is called, the excel spreadsheet has not been fully called yet, so it makes another active instance with the same name and has issues later on. I just have this check to make sure it has already passed the first turn and the excel spreadsheet has already opened only 1 time somewhere else. 
        currentKingdom.updateExcel()

    while True:
        option = input("Choose an option: ")
        option = option.lstrip(" ")
        option = option.rstrip(" ")
        if option == "1":
            currentKingdom.buy(input("Select what you would like to buy:\n"))
            option = ""
        elif option == "2":
            # print("MOVE SOMEONE")
            request = input("please input with the format [location] [character] [direction]\n(remember A for all, M for multiple, and x to go back) \nwho would you like to move:\n")
            currentKingdom.moveRequest(world_map, request, turn, kingdoms)
            # option = ""
        elif option == "4":
            gameOver = True
            break
        elif option == "3":
            for i in range(len(currentKingdom.lands)):
               if currentKingdom.lands[i].numAvailablePeasants > 0:
                   currentKingdom.buy(f"{i+1} {currentKingdom.lands[i].numAvailablePeasants} g")
            break

        # input("Press enter to continue:")
        clear_screen()
        # sys.stdout.write('\033[1m')  # make the header bold
        header(currentKingdom.name, turn, kingdoms)
        # sys.stdout.write('\033[0m')  # reset to normal font
        currentKingdom.printCities(turn)
        currentKingdom.updateExcel()

    return gameOver




def play_game(selected_options):
    kingdoms = defineKingdoms(selected_options)
    world_map = displayMap(kingdoms)

    turn = 0
    gameOver = False
    while not gameOver:
        turn += 1
        for team in kingdoms:
            if kingdoms[team].defeated == False:
                transitionPage(kingdoms[team].name)
                gameOver = takeTurn(turn, kingdoms, kingdoms[team], gameOver, world_map)
                if gameOver:
                    break
        if gameOver:
            break


