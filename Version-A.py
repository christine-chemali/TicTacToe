# Check if the board is completely filled
def board_full(board): 
    for row in board:  
        for cell in row: 
            if cell == " ":  # If an empty cell is found, board is not full
                return False  
    return True  # No empty cells, so board is full


# Get a valid move from the player
def player_move(player):
    while True:
        move = input(f"Joueur {player}, entrez votre mouvement : ") 
        
        # Check if the input is exactly two characters long
        if len(move) == 2: 
            try:
                line, column = int(move[0]), int(move[1])  # Convert input to integers
                
                # Ensure both row and column are between 0 and 2
                if 0 <= line <= 2 and 0 <= column <= 2:
                    return line, column
                else:
                    print("Veuillez entrer des chiffres entre 0 et 2.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer deux chiffres.")
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement deux chiffres.")

