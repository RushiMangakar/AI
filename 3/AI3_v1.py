import heapq  # To use a min-heap (priority queue)

def dijkstras_algorithm(graph, num_vertices, source):
    # List to store the shortest distance from the source to each vertex
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    
    # Min-heap for selecting the vertex with the minimum distance
    min_heap = [(0, source)]  # Start with the source vertex and distance 0
    
    while min_heap:
        dist, u = heapq.heappop(min_heap)
        
        # If the distance is already greater than the stored one, skip
        if dist > distances[u]:
            continue
        
        # Explore all the adjacent vertices
        for v in range(num_vertices):
            if graph[u][v] != 0:  # Check if an edge exists
                new_dist = dist + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))
    
    return distances

def create_graph(num_vertices):
    # Create an adjacency matrix with initial values of 0 (no self-connections)
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    
    print(f"Enter the connection weights for {num_vertices} vertices:")
    
    # Get the edge weights for the upper triangle of the adjacency matrix
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):  # Only need to input for i < j to avoid duplicates
            weight = int(input(f"Connection between vertex {i} and vertex {j}, Weight: "))
            graph[i][j] = weight
            graph[j][i] = weight  # Since the graph is undirected
    
    return graph

# Input the number of vertices
num_vertices = int(input("Enter the number of nodes/entities: "))

# Input the source vertex for Dijkstra's algorithm
source = int(input(f"Enter the source vertex (0 to {num_vertices - 1}): "))

# Create the graph based on user input
graph = create_graph(num_vertices)

# Run Dijkstra's algorithm on the graph
distances = dijkstras_algorithm(graph, num_vertices, source)

# Output the shortest path distances
print(f"\nShortest distances from vertex {source}:")
for i in range(num_vertices):
    print(f"Distance from {source} to {i}: {distances[i]}")

