import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g_cost = float('inf')  # Cost from start to this node
        self.h_cost = float('inf')  # Heuristic cost to target
        self.f_cost = float('inf')  # f_cost = g_cost + h_cost
        self.parent = None

    # Compare nodes based on f_cost for the priority queue
    def __lt__(self, other):
        return self.f_cost < other.f_cost

    # Define equality based on coordinates
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Hash function to make Node hashable for use in sets or as dictionary keys
    def __hash__(self):
        return hash((self.x, self.y))

def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_neighbors(node, grid):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for direction in directions:
        x, y = node.x + direction[0], node.y + direction[1]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':  # Blocked cells are 'X'
            neighbors.append(Node(x, y))
    return neighbors

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append((node.x, node.y))
        node = node.parent
    return path[::-1]

def a_star(start, target, grid):
    open_set = []
    closed_set = set()

    start.g_cost = 0
    start.h_cost = heuristic(start, target)
    start.f_cost = start.g_cost + start.h_cost

    heapq.heappush(open_set, start)

    while open_set:
        current = heapq.heappop(open_set)
        
        if current == target:
            return reconstruct_path(current)

        closed_set.add(current)

        for neighbor in get_neighbors(current, grid):
            if neighbor in closed_set:
                continue

            tentative_g_cost = current.g_cost + 1  # Assume cost between neighbors is always 1

            if tentative_g_cost < neighbor.g_cost:
                neighbor.g_cost = tentative_g_cost
                neighbor.h_cost = heuristic(neighbor, target)
                neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                neighbor.parent = current

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None  # If no path is found

# Function to display the grid visually with grid lines
def display_grid(grid, start, target):
    print("\nGrid Layout:")
    print("--------------")
    for i in range(3):
        row = "| "  # Start with the left border
        for j in range(3):
            if start.x == i and start.y == j:
                row += "S | "  # Start position
            elif target.x == i and target.y == j:
                row += "T | "  # Target position
            else:
                row += grid[i][j] + " | "  # Grid values ('O' for walkable, 'X' for obstacle)
        print(row)
        print("--------------")  # Row separator

# Function to take user input and build the grid
def get_user_input():
    grid = [[' ' for _ in range(3)] for _ in range(3)]  # Create a 3x3 grid initially with all 'O' (walkable)

    # Assign numbers (unique IDs) to each cell in the grid
    cell_number = 0
    cell_to_coords = {}  # Mapping cell_number to coordinates (i, j)
    for i in range(3):
        for j in range(3):
            cell_to_coords[cell_number] = (i, j)
            cell_number += 1  # Increment the number for the next cell
    
    print("Grid cell numbers have been assigned as follows:")
    display_grid(grid, Node(-1, -1), Node(-1, -1))  # Show grid with cell numbers

    # Now, prompt the user to place 'X' (obstacle) and 'O' (walkable) alternately
    print("You will now alternate placing 'X' (obstacle) and 'O' (walkable) for the cells.")
    print("Cell numbers range from 0 to 8 for a 3x3 grid.")
    
    updated_cells = set()  # Track updated cells
    total_cells = len(grid) * len(grid[0])

    for i in range(total_cells):
        if i % 2 == 0:
            # Prompt for 'X' cell (obstacle)
            while True:
                try:
                    cell_number_input = int(input(f"Enter cell number for 'X' (0 to 8): "))
                    if cell_number_input not in cell_to_coords:
                        print("Invalid cell number! Please choose a number between 0 and 8.")
                        continue
                    if cell_number_input in updated_cells:
                        print("This cell has already been updated. Please choose another cell.")
                        continue
                    x, y = cell_to_coords[cell_number_input]
                    grid[x][y] = 'X'  # Update the grid with 'X'
                    updated_cells.add(cell_number_input)  # Mark the cell as updated
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer between 0 and 8.")
        else:
            # Prompt for 'O' cell (walkable)
            while True:
                try:
                    cell_number_input = int(input(f"Enter cell number for 'O' (0 to 8): "))
                    if cell_number_input not in cell_to_coords:
                        print("Invalid cell number! Please choose a number between 0 and 8.")
                        continue
                    if cell_number_input in updated_cells:
                        print("This cell has already been updated. Please choose another cell.")
                        continue
                    x, y = cell_to_coords[cell_number_input]
                    grid[x][y] = 'O'  # Update the grid with 'O'
                    updated_cells.add(cell_number_input)  # Mark the cell as updated
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer between 0 and 8.")
        
        # Display the grid after each update
        display_grid(grid, Node(-1, -1), Node(-1, -1))

    # Ask the user for start and target positions
    start_cell = int(input("Enter the start cell number (0 to 8): "))
    target_cell = int(input("Enter the target cell number (0 to 8): "))

    start_x, start_y = cell_to_coords[start_cell]
    target_x, target_y = cell_to_coords[target_cell]
    
    # Display the final grid with start and target positions
    display_grid(grid, Node(start_x, start_y), Node(target_x, target_y))
    
    return grid, Node(start_x, start_y), Node(target_x, target_y)

# Main execution
grid, start, target = get_user_input()

path = a_star(start, target, grid)

if path:
    print("Path found:", path)
else:
    print("No path found")

