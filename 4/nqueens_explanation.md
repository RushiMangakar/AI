
# N-Queens Solver Implementation Explanation

## Function Breakdown

### 1. is_safe(board, row, col, n)
This function checks if it's safe to place a queen at position (row, col)
- Checks horizontally to the left for other queens
- Checks upper left diagonal for other queens
- Checks lower left diagonal for other queens
Returns True if safe, False otherwise

```python
# Pseudocode for is_safe:
Function is_safe(board, row, col, n):
    Check left side of row for queens
    Check upper left diagonal for queens
    Check lower left diagonal for queens
    Return true if no conflicts found
```

### 2. solve_n_queens_limited(board, col, n, solutions, required_solutions)
Recursive function that attempts to place queens column by column
- Base case: If col >= n, a solution is found
- For each row in current column:
  - Check if safe to place queen
  - If safe, place queen and recurse
  - If not successful, backtrack
Returns True when enough solutions are found

```python
# Pseudocode for solve_n_queens_limited:
Function solve_n_queens_limited(board, col, n, solutions, required_solutions):
    If column >= n:
        Add current board to solutions
        Return true if we have enough solutions
    
    For each row in current column:
        If safe to place queen:
            Place queen
            Recurse for next column
            If enough solutions found, return true
            Remove queen (backtrack)
    Return false
```

### 3. find_solutions(n, required_solutions)
Main function to initialize board and find solutions
- Creates empty n×n board
- Calls recursive solver
- Returns list of solutions

### 4. print_solutions(solutions, required_solutions)
Output function to display solutions
- Prints total number of solutions found
- Displays each solution as a grid

## Line-by-Line Explanation

```python
# Main components explanation
board[i][col] = 1       # Places queen at position (i, col)
board[i][col] = 0       # Removes queen (backtracking)

# Diagonal checks using zip:
zip(range(row, -1, -1), range(col, -1, -1))    # Upper left diagonal
zip(range(row, n, 1), range(col, -1, -1))      # Lower left diagonal

# Board representation:
# 0 = empty square
# 1 = queen placed
[[0 for _ in range(n)] for _ in range(n)]      # Creates empty n×n board
```

## Time Complexity
- Time Complexity: O(N!)
- Space Complexity: O(N²)

## Implementation Details
1. The program uses a backtracking approach
2. Queens are placed column by column
3. Solutions are stored as 2D arrays
4. The algorithm stops when the required number of solutions is found
5. Input validation ensures positive values for board size and solution count
