def dfs_disconnected(graph):

    visited = set()
    result=[]

    def dfs(node):

        visited.add(node)

        result.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                dfs(neighbor)

    for node in graph:

        if node not in visited:

            dfs(node)
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
    'E': ['F'],
    'F': ['E']
}

print(dfs_disconnected(graph))