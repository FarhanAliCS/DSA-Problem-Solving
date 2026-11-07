def remove_vertex(graph , vertex):
    if vertex not in graph:
        print("Vertex is not in graph .")
        return
    for node in graph:
        if vertex in graph[node]:
            graph[node].remove(vertex)
    del graph[vertex]


graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['B','E'],
    'E':['C','D'],
    'F':[]
}
remove_vertex(graph , "A")
print(graph)

        
    
    

