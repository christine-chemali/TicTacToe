#CREATE THE BOARD

def show_board(board):
    print(" ")  
    print(" "*13," TIC TAC TOE ", " "*13)
    print(" ")  
    print(" "*13,"-" * 13," "*13)
    for row in board: 
        print(" " * 13,"|", row[0], "|", row[1], "|", row[2], "|"," " * 13)  
        print(" "*13,"-" * 13," "*13) 
    print(" ")  

#CHECK FOR VICTORY

def victory(board, player): 
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

def player_move(player):
    while True:
        move = input(f"Joueur {player}, entrez votre mouvement (ligne colonne) : ") 
        if len(move) == 2: 
            try:
                line = int(move[0])
                column = int(move[1])
                if 0 <= line <= 2 and 0 <= column <= 2:
                    return line, column
                else:
                    print("Veuillez entrer des chiffres entre 0 et 2.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer deux chiffres.")
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement deux chiffres.")

# PLAY

def game_tic_tac_toe(): 
    board = [] 
    for a in range(3):  
        row = []
        for a in range(3):  
            row.append(' ')  
        board.append(row)  
    actual_player = 'X'
    
    while True:
        show_board(board)
        line, column = player_move(actual_player)
        
        if board[line][column] == ' ':
            board[line][column] = actual_player
            if victory(board, actual_player):
                show_board(board)
                print(f"Félicitations ! Joueur {actual_player} a gagné !")
                break
            elif board_full(board):
                show_board(board)
                print("Match nul !")
                break
            actual_player = 'O' if actual_player == 'X' else 'X'
        else:
            print("Cette case est déjà occupée. Essayez à nouveau.")
game_tic_tac_toe()   


