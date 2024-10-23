def Tictactoe(board):
    for j in range(0, 9, 3):
        print("________")
        print("|" + "|".join(board[j:j+3]) + "|")
    print("________")

def check_win(board):
    lines = [board[i:i+3] for i in range(0, 9, 3)]
    colonum = [board[i::3] for i in range(3)]
    diago = [[board[0], board[4],board[8]], [board[2], board[4], board[6]]]
    return any(all(cell == player != ' ' for cell in line) for player in ['X', 'O'] for line in lines + colonum + diago)

def tic_tac_toe():
    board, players, turn = [' '] * 9, ['X', 'O'], 0
    while ' ' in board:
        print(f"Player{players[turn % 2]}")
        Tictactoe(board)
        while True:
            try:
                case = int(input("Choose a case (1-9) : ")) - 1
                if board[case] == ' ':
                    board[case] = players[turn % 2]
                    break
                print("No possible. Try again.")
            except (ValueError, IndexError):
                print("Invalide. Try again.")
        if check_win(board):
            Tictactoe(board)
            print(f"Player {players[turn % 2]} Win !")
            return
        turn += 1
    Tictactoe(board)
    print("No Winners!")

if __name__ == "__main__":
    tic_tac_toe()

