from collections import deque
def bfs(graph , start):
    visited=set()
    queue=deque([start])
    result=[]
    visited.add(start)
    while queue:
        remove=queue.popleft()
        result.append(remove)
        for neigbor in graph[remove]:
            if neigbor not in visited:
                visited.add(neigbor)
                queue.append(neigbor)
    return result
                
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B'],
    'F':['C']
}
print(bfs(graph , 'A'))