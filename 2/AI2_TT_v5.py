import heapq

class Node:
    def __init__(self, x, y, board, player):
        self.x = x
        self.y = y
        self.board = board
        self.player = player
        self.g_cost = float('inf')  # Cost from start to this node
        self.h_cost = float('inf')  # Heuristic cost to target
        self.f_cost = float('inf')  # f_cost = g_cost + h_cost
        self.parent = None

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.board == other.board

    def __hash__(self):
        return hash((self.x, self.y, str(self.board)))


def heuristic(a, b):
    # A simple heuristic that assumes we're just looking for potential moves
    return 0

def get_neighbors(node, player):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if node.board[i][j] == ' ':
                new_board = [row[:] for row in node.board]  # Copy the board
                new_board[i][j] = player  # Simulate placing the player's mark
                neighbors.append(Node(i, j, new_board, player))
    return neighbors


def check_winner(board, player):
    # Check rows and columns for a win
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


def find_block_move(board, player):
    # Look for a move that blocks the opponent from winning
    opponent = 'O' if player == 'X' else 'X'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = [row[:] for row in board]
                new_board[i][j] = opponent
                if check_winner(new_board, opponent):
                    return i, j
    return None


def display_board(board):
    print("\nBoard Layout:")
    print("--------------")
    for i in range(3):
        row = "| "  # Start with the left border
        for j in range(3):
            row += board[i][j] + " | "  # Board values ('O' for walkable, 'X' for obstacle)
        print(row)
        print("--------------")  # Row separator


def a_star(start, player):
    open_set = []
    closed_set = set()

    start.g_cost = 0
    start.h_cost = heuristic(start, None)
    start.f_cost = start.g_cost + start.h_cost

    heapq.heappush(open_set, start)

    while open_set:
        current = heapq.heappop(open_set)

        # Check if the current board is a winning board for the AI
        if check_winner(current.board, player):
            return [(current.x, current.y)]

        closed_set.add(current)

        for neighbor in get_neighbors(current, player):
            if neighbor in closed_set:
                continue

            tentative_g_cost = current.g_cost + 1
            if tentative_g_cost < neighbor.g_cost:
                neighbor.g_cost = tentative_g_cost
                neighbor.h_cost = heuristic(neighbor, None)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                neighbor.parent = current

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None


def is_tie(board):
    # Check if the board is full and there is no winner
    for row in board:
        if ' ' in row:
            return False  # Still have empty spaces, so not a tie
    return True


def tic_tac_toe():
    # Ask the user if they want to play with another player or against the computer
    mode = input("1. Player vs Player \n2. Player vs Computer \nChoose game mode:  ")

    # Initialize the 3x3 board with empty spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 'X'  # Player X goes first
    moves_left = 9

    while moves_left > 0:
        display_board(board)

        if mode == '1':  # Player vs Player
            # Alternate turns between two players (X and O)
            print(f"Player {turn}'s turn:")
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
        else:  # Player vs Computer
            if turn == 'X':
                # Player X makes a move (human)
                print(f"Player {turn}'s turn:")
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
            else:
                # AI (Player O) makes a move
                print(f"AI (Player {turn})'s turn:")

                # Check if Player X is about to win (block that move)
                block_move = find_block_move(board, 'O')
                if block_move:
                    print(f"AI blocks Player X's winning move at cell {block_move[0]*3 + block_move[1]}")
                    board[block_move[0]][block_move[1]] = 'O'
                else:
                    # If Player X is not about to win, use A* to find the best move
                    start_node = Node(0, 0, board, 'O')  # Initial state
                    move = a_star(start_node, 'O')

                    if move:
                        best_move = move[-1]  # The last position in the reconstructed path
                        row, col = best_move
                        board[row][col] = turn
                        moves_left -= 1
                        print(f"AI places 'O' in cell {row*3 + col}")

        # Check if the current player has won
        if check_winner(board, turn):
            display_board(board)
            print(f"Player {turn} wins!")
            return  # Game over, exit the function

        # Check for tie (draw) if there are no more moves left and no winner
        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            return  # Game over, exit the function

        # Switch turns between 'X' and 'O'
        turn = 'O' if turn == 'X' else 'X'


# Start the Tic-Tac-Toe game
tic_tac_toe()
