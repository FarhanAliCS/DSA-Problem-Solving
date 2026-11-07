def total_weight(graph):
    if not graph:
        return 0
    total=0
    for vertex in graph:
        for neighbor , weight in graph[vertex]:
            total+=weight

    return total//2
graph={
    'A':[('B',5),('C',10)],
    'B':[('A',5),('D',3)],
    'C':[('A',10),('D',7)],
    'D':[('B',3),('C',7)]
}
print("Total weight :" ,total_weight(graph))
