
## Explanation of Functions

### `is_safe(board, row, col, n)`

This function checks if it's safe to place a queen at position (row, col) on the board.

- **Parameters:**
  - `board`: The current state of the board.
  - `row`: The row index where the queen is to be placed.
  - `col`: The column index where the queen is to be placed.
  - `n`: The size of the board (n x n).

- **Returns:** `True` if it's safe to place the queen, `False` otherwise.

#### Code Explanation:
```python
def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True
```

### `solve_n_queens_util(board, col, n)`

This function uses recursion and backtracking to solve the n-queens problem.

- **Parameters:**
  - `board`: The current state of the board.
  - `col`: The current column index to place the queen.
  - `n`: The size of the board (n x n).

- **Returns:** `True` if a solution is found, `False` otherwise.

#### Code Explanation:
```python
def solve_n_queens_util(board, col, n):
    # base case: If all queens are placed then return true
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then
            # remove queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in this column col then return false
    return False
```

### `solve_n_queens(n)`

This function initializes the board and calls the utility function to solve the problem.

- **Parameters:**
  - `n`: The size of the board (n x n).

- **Returns:** `True` if a solution is found, `False` otherwise.

#### Code Explanation:
```python
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True
```

### `print_solution(board)`

This function prints the board configuration.

- **Parameters:**
  - `board`: The current state of the board.

#### Code Explanation:
```python
def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
```

## Pseudocode

```
function is_safe(board, row, col, n):
    for i from 0 to col-1:
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

function solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    for i from 0 to n-1:
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[i][col] = 0

    return False

function solve_n_queens(n):
    board = create n x n matrix filled with 0

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

function print_solution(board):
    for each row in board:
        print row as string
```
