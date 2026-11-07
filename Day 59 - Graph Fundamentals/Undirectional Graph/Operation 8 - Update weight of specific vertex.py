def update_edge_weight(graph,node1, node2, new_weight):
    if node1 not in graph or node2 not in graph:
        return None
    edge_found=False
    for i ,(neigbor,weight) in enumerate(graph[node1]):
        if neigbor == node2:
            graph[node1][i] = (node2,new_weight)
            edge_found=True
            break

    if not edge_found:
        print("Edge does not exists")
        return
    for i,(neighbor,weight) in enumerate(graph[node2]):
        if neighbor == node1:
            graph[node2][i] = (node1 , new_weight)
            break
    print("edge weight update succesfully .")
    

graph={
    'A':[('B',5),('C',10)],
    'B':[('A',5),('D',3)],
    'C':[('A',10),('D',7)],
    'D':[('B',3),('C',7)]
}
update_edge_weight(graph , 'A','B',15)
print(graph)
