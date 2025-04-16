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
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
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

# Example usage

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],  # 1's represent obstacles
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = Node(0, 0)
target = Node(4, 4)

path = a_star(start, target, grid)

if path:
    print("Path found:", path)
else:
    print("No path found")

