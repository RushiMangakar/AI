def dfs(graph, start):
	visited = set()
	stack = [start]
	
	while stack:
		node = stack.pop()
		
		if node not in visited:
			visited.add(node)
			print(node, end=' ')
			
		
			for neighbor in graph[node]:
				if neighbor not in visited:
					stack.append(neighbor)
					
					
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

dfs(graph,'A')
print("\n")
