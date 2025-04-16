import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name  # Node's identifier (e.g., (x, y) position)
        self.parent = parent  # Parent node
        self.g = g  # Cost to reach the current node
        self.h = h  # Heuristic estimate to the goal node
        self.f = g + h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f  # This is for the priority queue to compare nodes based on f

def a_star(start, goal, get_neighbors, heuristic):
    # OPEN list: nodes to be evaluated
    open_list = []
    # CLOSED list: nodes already evaluated
    closed_list = set()

    # Initialize the start node
    start_node = Node(start, g=0, h=heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)

        # If the goal node is reached, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return the reversed path (from start to goal)

        # Add current node to the CLOSED list
        closed_list.add(current_node.name)

        # Get the neighbors of the current node
        for neighbor in get_neighbors(current_node.name):
            if neighbor in closed_list:
                continue  # Ignore already evaluated nodes

            g_cost = current_node.g + 1  # Assuming uniform cost for each step
            h_cost = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, parent=current_node, g=g_cost, h=h_cost)

            # Check if the neighbor is already in the OPEN list with a higher cost
            if all(neighbor_node.f < node.f for node in open_list if node.name == neighbor_node.name):
                heapq.heappush(open_list, neighbor_node)

    return None  # If the goal is unreachable

# Example heuristic function (Manhattan Distance for a grid-based problem)
def heuristic(node, goal):
    # Example: Manhattan distance for 2D grid (can be customized for your problem)
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Example function to get neighbors (for grid-based search)
def get_neighbors(node):
    x, y = node
    neighbors = [
        (x + 1, y),  # Right
        (x - 1, y),  # Left
        (x, y + 1),  # Up
        (x, y - 1),  # Down
    ]
    # You could add boundary checks here to prevent going outside of the grid
    return neighbors

# Example usage
start = (0, 0)
goal = (4, 4)
path = a_star(start, goal, get_neighbors, heuristic)

if path:
    print("Path found:", path)
else:
    print("No path found.")

