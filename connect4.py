# Connect 4 in python

# Rack is 6 rows x 7 columns
# Player must connect 4 discs in a row (horizontal, vertical or diagonal)
import numpy as np
import time

ROWS = 6
COLUMNS = 7

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

# The actual game
def game():
    game_over = False
    winner = 0
    board = create_board()
    turn = 0
    
    # Loops between players
    while game_over != True:

        print(board)
        print("\n")

        # PLAYER 1 TURN
        if turn == 0:
            try:
                column = int(input("Player 1, make your selection (1-7): \n"))
                # Makes sure player picks a valid column
                while column < 1 or column > 7:
                    column = int(input("Player 1, make your selection (1-7): \n"))

                for i in range(len(board) - 1, -1, -1):
                    # Checks if column is full
                    if (board[0][column - 1] == 0):
                        if (board[i][column - 1] == 0):
                            board[i][column - 1] = 1
                            game_over = check_for_win(board, 1)
                            break
                    else:
                        # If column is full, asks player 1 for another slot
                        turn = -1
                    
                    
            except ValueError:
                print("Invalid input! Please enter your column between (1 - 7)!")
                turn = -1

        # PLAYER 2's TURN
        else:           
            try:
                column = int(input("Player 2, make your selection (1-7): \n"))
                # Makes sure player picks a valid column
                while column < 1 or column > 7:
                    column = int(input("Player 2, make your selection (1-7): \n"))
                
                for i in range(len(board) - 1, -1, -1):
                    if (board[0][column - 1] == 0):
                        if (board[i][column - 1] == 0):
                            board[i][column - 1] = 2
                            game_over = check_for_win(board, 2)
                            break
                    else:
                        # If column is full, will ask player 2 to choose another slot
                        turn = 0
                
                    
                        
            except ValueError:
                print("Invalid input! Please enter your column between (1 - 7)!")
                turn = 0
        
        turn += 1
        # resets turn number to 0 if turn = 2
        turn = turn % 2

    replay()


def check_for_win(board, piece):
    horizontal = horizontal_check(board, piece)
    vertical = vertical_check(board, piece)
    diagonal = diagonal_check(board, piece)

    if (horizontal or vertical or diagonal):
        time.sleep(1)
        print("\nPlayer {} wins! Congratulations!\n".format(str(piece)))
        print(board)

    return horizontal or vertical or diagonal

def horizontal_check(board, piece):
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if (board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece):
                return True
            
def vertical_check(board, piece):
    for r in range(ROWS - 3):
        for c in range(COLUMNS):
            if (board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece):
                return True
            
def diagonal_check(board, piece):
    # Facing right check
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if (board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
                return True
    
    # Facing left check

    for c in range(6, COLUMNS - 5, -1):
        for r in range(3, ROWS):
            if (board[r][c] == piece and board[r - 1][c - 1] == piece and board[r - 2][c - 2] == piece and board[r - 3][c - 3] == piece):
                return True


# Creates the empty board
def create_board():
    board = np.zeros((6, 7))
    return board

def replay():
    print("Nice balls bro")
    play_again = input("Would you like to play again? (y/n): ")
    
    print(play_again)

    if (play_again == "y"):
        print("Now restarting game...")
        time.sleep(2)
        intro()
    elif (play_again == "n"):
        print("Thanks for playing! See you again soon....")
        time.sleep(2)
        quit()
    else:
        print("Invalid input!")
        replay()

#intro()

replay()