def add_vertex(graph,vertex):
    if vertex in graph:
        print("Vertex already exist .")
        return
    graph[vertex]=[]
    print(f"Vertex {vertex} add succesfully .")

graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['B','E'],
    'E':['C','D']
}
add_vertex(graph , "F")
print(graph)

        
    
    
