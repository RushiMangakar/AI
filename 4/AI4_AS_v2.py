def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def add_solution(board, solutions):
    solution = []
    for row in board:
        solution.append(row.copy())
    solutions.append(solution)

def solve_n_queens_all(board, col, n, solutions):
    if col >= n:
        add_solution(board, solutions)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_all(board, col + 1, n, solutions)
            board[i][col] = 0

def find_all_solutions(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_all(board, 0, n, solutions)
    return solutions

def print_all_solutions(solutions):
    if not solutions:
        print("No solutions exist")
        return

    print(f"Total number of solutions: {len(solutions)}")
    for i, solution in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for row in solution:
            print(" ".join(str(x) for x in row))
        print()

n = 8
solutions = find_all_solutions(n)
print_all_solutions(solutions)
