# PLAY

def game_tic_tac_toe(): 
    board = [] 
    for row_index in range(3):  
        row = []
        for column_index in range(3):  
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

