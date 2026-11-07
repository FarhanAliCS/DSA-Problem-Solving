def add_edge(graph , node1 , node2):
    if node1 not in graph or node2 not in graph:
        print("Edge does not exist .")
        return
    if node2 in graph[node1]:
        print("Edge already exists")
        return
    graph[node1].append(node2)
    graph[node2].append(node1)

def remove_edge(graph,node1,node2):
    if node1 not in graph or node2 not in graph:
        print("Vertix does not exists .")
        return
    if node2 not in graph[node1]:
        print("Vertix does not exists .")
        return
    graph[node1].remove(node2)
    graph[node2].remove(node1)
graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['B','E'],
    'E':['C','D']
}

add_edge(graph , 'A','D')
remove_edge(graph,'A','D')
print(graph)