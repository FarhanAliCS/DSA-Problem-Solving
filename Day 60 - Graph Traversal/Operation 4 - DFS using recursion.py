def dfs_recursive(graph, start):

    visited = set()
    result = []

    def dfs(node):

        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)

    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print(dfs_recursive(graph, 'A'))