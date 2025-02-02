def generate_permutations(arr):
    if len(arr) <= 1:
        return [arr]
    
    perms = []
    for i in range(len(arr)):
        # Remove current element
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        
        # Generate permutations of remaining elements
        for p in generate_permutations(remaining):
            perms.append([current] + p)
    
    return perms

def traveling_salesman_bruteforce(graph):
    nodes = list(graph.keys())
    shortest_path = float('inf')
    
    for path in generate_permutations(nodes[1:]):  # Start from node 0
        current_path_length = graph[nodes[0]][path[0]]  # First edge
        
        # Calculate path length
        for i in range(len(path) - 1):
            current_path_length += graph[path[i]][path[i + 1]]
        
        # Add return to start
        current_path_length += graph[path[-1]][nodes[0]]
        
        shortest_path = min(shortest_path, current_path_length)
    
    return shortest_path
