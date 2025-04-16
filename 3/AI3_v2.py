def dijkstras_algorithm(graph, num_vertices, source):
    distances = [float('inf')] * num_vertices
    distances[source] = 0
    
    visited = [False] * num_vertices
    
    for _ in range(num_vertices):
        min_distance = float('inf')
        u = -1
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                u = v
                
        visited[u] = True
        
        for v in range(num_vertices):
            if graph[u][v] != 0 and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
    
    return distances

def create_graph(num_vertices):
    graph = [[0] * num_vertices for _ in range(num_vertices)]
    
    print(f"Enter the connection weights for {num_vertices} vertices:")
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices): 
            weight = int(input(f"Connection between vertex {i} and vertex {j}, Weight: "))
            graph[i][j] = weight
            graph[j][i] = weight
    
    return graph

num_vertices = int(input("Enter the number of nodes/entities: "))
source = int(input(f"Enter the source vertex (0 to {num_vertices - 1}): "))
graph = create_graph(num_vertices)
distances = dijkstras_algorithm(graph, num_vertices, source)
print(f"\nShortest distances from vertex {source}:")
for i in range(num_vertices):
    print(f"Distance from {source} to {i}: {distances[i]}")


