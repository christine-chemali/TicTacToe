#CREATE THE BOARD
def show_board(board):
    print(" ")  
    print(" " * 13, " TIC TAC TOE ", " " * 13)
    print(" ")
    print("Pour jouer, entrez le numéro de la ligne")
    print("et celui de la colonne. Exemple: 00")  
    print(" ")   
    print(" " * 13, " ", "0 ", " 1 ", " 2 ", " " * 13) 
    print(" " * 13, "-" * 13, " " * 13)
    for index, row in enumerate(board):
        print(" " * 11, index, "|", row[0], "|", row[1], "|", row[2], "|", " " * 13)   
        print(" " * 13, "-" * 13, " " * 13) 
    print(" ")   

#CHECK FOR VICTORY

def victory(board, player): # check rows, columns, and diagonals for a win
    for row in range(3):   
        if board[row][0] == player and board[row][1] == player and board[row][2] == player: 
            return True 
    for col in range(3):  
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True  
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True   
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: 
        return True   
    return False 

#CHECK IF BOARD IS FILLED COMPLETELY OR NOT

def board_full(board): 
    for row in board:  
        for cell in row: 
            if cell == " ": 
                return False  
    return True 

# PLAYER MOVE

def player_move(player): # get a valid move from the player
    while True: 
        move = input(f"Joueur {player}, entrez votre mouvement : ") 
        if len(move) == 2:  # if the entry has 2 characters
            try:
                line = int(move[0]) # convert input in an integer 
                column = int(move[1])
                if 0 <= line <= 2 and 0 <= column <= 2: # insure that values are betweeen 0 and 2
                    return line, column
                else:
                    print("Veuillez entrer des chiffres entre 0 et 2.")
            except ValueError: # handle invalid input (letter)
                print("Entrée invalide. Veuillez entrer deux chiffres.")
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement deux chiffres.")

# PLAY

def game_tic_tac_toe(): 
    board = [] # initiate an empty board list with 3 row lists, each filled with empty spaces
    for row_index in range(3):  
        row = []
        for column_index in range(3):  
            row.append(' ')  
        board.append(row)  
    actual_player = 'X'  
    
    while True: # continue until a winner is found or the board is full
        show_board(board) 
        line, column = player_move(actual_player) 
        
        if board[line][column] == ' ': 
            board[line][column] = actual_player 
            if victory(board, actual_player): # check for a win condition
                show_board(board)
                print(f"Félicitations ! Joueur {actual_player} a gagné !")
                break 
            elif board_full(board): # check if the board is full, draw condition
                show_board(board)
                print("Match nul !")
                break 
            actual_player = 'O' if actual_player == 'X' else 'X' # switch the player 
        else:
            print("Cette case est déjà occupée. Essayez à nouveau.")
game_tic_tac_toe()   # start the game


