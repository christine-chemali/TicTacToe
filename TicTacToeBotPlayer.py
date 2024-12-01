# CREATE THE BOARD
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

# CHECK FOR VICTORY
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

# BOARD FULL
def board_full(board):
    for row in board: 
        for cell in row:
            if cell == " ": 
                return False 
    return True 

# PLAYER MOVE
def player_move(player_name, board): 
    while True:
        move = input(f"{player_name}, entrez votre mouvement (ligne colonne) : ")
        if len(move) == 2: 
            try:
                line = int(move[0]) 
                column = int(move[1])
                if 0 <= line <= 2 and 0 <= column <= 2:
                    if board[line][column] == ' ':
                        return line, column
                    else:
                        print("Cette case est déjà occupée. Essayez à nouveau.")
                else:
                    print("Veuillez entrer des chiffres entre 0 et 2.")
            except ValueError: 
                print("Entrée invalide. Veuillez entrer deux chiffres.")
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement deux chiffres.")

# BOT MOVE
def bot_move(board, bot, human):
    if board[1][1] == ' ':
        return 1, 1
    for row in range(3): 
        for column in range(3):
            if board[row][column] == ' ':
                board[row][column] = bot
                if victory(board, bot):
                    return row, column  
                board[row][column] = ' ' 
    for row in range(3):  
        for column in range(3):
            if board[row][column] == ' ':
                board[row][column] = human
                if victory(board, human):
                    board[row][column] = ' '  
                    return row, column  
                board[row][column] = ' '  
    for row in range(3): 
        for column in range(3):
            if board[row][column] == ' ':
                return row, column 
    return -1, -1  

# GAME PLAY FUNCTION
def game_tic_tac_toe(): 
    print(" ") 
    print(" " * 13, " TIC TAC TOE ", " " * 13)
    print(" ")
    while True:
        mode = input("Voulez-vous jouer contre un autre joueur (1) ou contre le bot (2)? Entrez 1 ou 2: ")    
        if mode == '1':
            player1_name = input("Entrez le nom du joueur 1 : ")
            player2_name = input("Entrez le nom du joueur 2 : ")
            break  
        if mode == '2':
            player1_name = input("Entrez votre nom : ")
            player2_name = "Bot"
            break 
        print("Choix invalide, veuillez entrer 1 ou 2.")  

    board = [[' ' for _ in range(3)] for _ in range(3)]
    actual_player = 'X'
    player_names = { 'X': player1_name, 'O': player2_name }
   
    while True:
        show_board(board)        
        if player_names[actual_player] == "Bot":
            print("Le bot réfléchit...")
            line, column = bot_move(board, 'O', 'X')
            if board[line][column] == ' ':
                board[line][column] = 'O'
                if victory(board, 'O'):
                    show_board(board)
                    print("Le bot a gagné !")
                    break
        else:
            line, column = player_move(player_names[actual_player], board) 
            board[line][column] = actual_player
        if victory(board, actual_player):
            show_board(board)
            print(f"Félicitations ! {player_names[actual_player]} a gagné !")
            break
        elif board_full(board):
            show_board(board)
            print("Match nul !")
            break

        actual_player = 'O' if actual_player == 'X' else 'X'

game_tic_tac_toe()