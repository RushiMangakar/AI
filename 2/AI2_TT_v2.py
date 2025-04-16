def display_board(board):
    print("\nBoard Layout:")
    print("--------------")
    for i in range(3):
        row = "| "  # Start with the left border
        for j in range(3):
            row += board[i][j] + " | "  # Board values ('O' for walkable, 'X' for obstacle)
        print(row)
        print("--------------")  # Row separator


def check_winner(board, player):
    # Check rows and columns
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def tic_tac_toe():
    # Initialize the 3x3 board with empty spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'  # Player X goes first
    moves_left = 9

    while moves_left > 0:
        # Display the current board
        display_board(board)
        print(f"Player {turn}'s turn:")
        
        # Take input for the move (cell number 0-8)
        while True:
            try:
                cell = int(input(f"Enter a cell number (0-8): "))
                if cell < 0 or cell > 8:
                    print("Invalid cell number! Please enter a number between 0 and 8.")
                    continue
                
                # Convert cell number to coordinates (row, col)
                row, col = divmod(cell, 3)

                # Check if the selected cell is already occupied
                if board[row][col] != ' ':
                    print("This cell is already taken. Please choose another cell.")
                    continue
                
                # Place the player's mark ('X' or 'O') in the chosen cell
                board[row][col] = turn
                moves_left -= 1
                break
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 8.")

        # Check if the current player has won
        if check_winner(board, turn):
            display_board(board)
            print(f"Player {turn} wins!")
            return  # Game over, exit the function

        # Check for draw
        if moves_left == 0:
            display_board(board)
            print("It's a draw!")
            return  # Game over, exit the function

        # Switch turns between 'X' and 'O'
        turn = 'O' if turn == 'X' else 'X'


# Start the Tic-Tac-Toe game
tic_tac_toe()

