def get_edge_weight(graph , node1 , node2):
    if node1 not in graph or node2 not in graph:
        print("vertex does not exists .")
        return 
    for neigbor , weight in graph[node1]:
        if neigbor == node2:
            return weight
    print("edge does not exists")
    return

graph={
    'A':[('B',5),('C',10)],
    'B':[('A',5),('D',3)],
    'C':[('A',10),('D',7)],
    'D':[('B',3),('C',7)]
}
print(get_edge_weight(graph , 'A','B'))