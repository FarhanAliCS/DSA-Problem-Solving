def dfs(graph , start):
    visited=set()
    result=[]
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
                
    return result


    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
print(dfs(graph,'A'))