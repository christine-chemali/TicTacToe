"""
def main():
    # The main function
    board = create_grid()
    pretty = printPretty(board)
    player1_symbol, player2_symbol = sym()
    full = isFull(board, player1_symbol, player2_symbol)  # Starts the game


def create_grid():
    # Playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board


def sym():
    # Players' symbols
    player1_symbol = input("Player 1, do you want to be X or O? ")
    if player1_symbol == "X":
        player2_symbol = "O"
        print("Player 2, you are O.")
    else:
        player2_symbol = "X"
        print("Player 2, you are X.")
    input("Press enter to continue.")
    print("\n")
    return player1_symbol, player2_symbol


def startGamming(board, player1_symbol, player2_symbol, count):
    # starts the game.
    
    # the turn
    if count % 2 == 0:
        player_symbol = player1_symbol
    else:
        player_symbol = player2_symbol
    
    print(f"Player {player_symbol}, it is your turn.")
    
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column enter 2]"))
"""

def create_grid():
    # playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def printPretty(board):
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")

# Testing 
board = create_grid()
printPretty(board)
