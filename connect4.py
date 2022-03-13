# Connect 4 in python

# Rack is 6 rows x 7 columns
# Player must connect 4 discs in a row (horizontal, vertical or diagonal)
import time

def intro():

    print("""
     .o88b.  .d88b.  d8b   db d8b   db d88888b  .o88b. d888888b   j88D    d8888b. db    db d888888b db   db  .d88b.  d8b   db 
    d8P  Y8 .8P  Y8. 888o  88 888o  88 88'     d8P  Y8 `~~88~~'  j8~88    88  `8D `8b  d8' `~~88~~' 88   88 .8P  Y8. 888o  88 
    8P      88    88 88V8o 88 88V8o 88 88ooooo 8P         88    j8' 88    88oodD'  `8bd8'     88    88ooo88 88    88 88V8o 88 
    8b      88    88 88 V8o88 88 V8o88 88~~~~~ 8b         88    V88888D   88~~~      88       88    88~~~88 88    88 88 V8o88 
    Y8b  d8 `8b  d8' 88  V888 88  V888 88.     Y8b  d8    88        88    88         88       88    88   88 `8b  d8' 88  V888 
     `Y88P'  `Y88P'  VP   V8P VP   V8P Y88888P  `Y88P'    YP        VP    88         YP       YP    YP   YP  `Y88P'  VP   V8P                                                                                                                          
                                                                                                                          """)

    try:
        start = int(input("1.Play\n2.How to play\n\n"))
        if (start == 1):
            time.sleep(1)
            game()
        elif (start == 2):
            print("The main objective of the game of Connect 4 is for players to slot 4 of their discs into the rack and be able to get them all in a row (4 in a row).\nThe gameplay is quite similar to that of Tic-Tac-Toe in that the pieces must all be placed 4-in-a-row vertically, horizontally, or diagonally in order for a player to claim a win.")
            time.sleep(3)
            main = input("Press enter to return to the menu: ")
            while (main != ""):
                main = input("Press enter to return to the menu: ")
            intro()
        else:
            print("Invalid input!")
            intro()

    except ValueError:
        print("Invalid input!")
        intro()

def game():
    board = [   
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]            
            ]

intro()