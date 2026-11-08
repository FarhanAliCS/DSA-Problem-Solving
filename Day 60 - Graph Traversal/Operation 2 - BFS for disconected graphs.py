from collections import deque
def bfs_all(graph):
    visited=set()
    result=[]
    
    for node in graph:
        if node not in visited:
            queue=deque([node])
            visited.add(node)
        while queue:
            current=queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return result
    
graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A'],
    'D':['B'],
    'E':['F'],
    'F':['E']
}
print(bfs_all(graph))