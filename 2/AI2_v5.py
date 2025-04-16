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

# Function to display the grid visually
def display_grid(grid, start, target):
    print("\nGrid Layout:")
    for i in range(3):
        row = ""
        for j in range(3):
            if start.x == i and start.y == j:
                row += "S "  # Start position
            elif target.x == i and target.y == j:
                row += "T "  # Target position
            else:
                row += grid[i][j] + " "  # Grid values ('O' for walkable, 'X' for obstacle)
        print(row)
    print()

# Function to take user input and build the grid
def get_user_input():
    grid = [[None for _ in range(3)] for _ in range(3)]  # Create a 3x3 grid with placeholders

    # Assign numbers (unique IDs) to each cell in the grid
    cell_number = 0
    for i in range(3):
        for j in range(3):
            grid[i][j] = str(cell_number)  # Assign the unique cell number as a string
            cell_number += 1  # Increment the number for the next cell
    
    print("Grid cell numbers have been assigned as follows:")
    display_grid(grid, Node(-1, -1), Node(-1, -1))  # Show grid with cell numbers

    # Now, prompt the user for each cell's walkability ('O' = walkable, 'X' = obstacle)
    for i in range(3):
        for j in range(3):
            while True:
                value = input(f"Enter value for cell ({i},{j}) (O for walkable, X for obstacle) [{grid[i][j]}]: ").strip().upper()
                if value not in ['O', 'X']:
                    print("Invalid input! Please enter 'O' for walkable or 'X' for obstacle.")
                    continue
                grid[i][j] = value
                break

    # Display the grid after it has been fully entered
    display_grid(grid, Node(-1, -1), Node(-1, -1))  # Show grid after values are entered

    start_x, start_y = map(int, input("Enter the start coordinates (x y): ").split())
    target_x, target_y = map(int, input("Enter the target coordinates (x y): ").split())
    
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

