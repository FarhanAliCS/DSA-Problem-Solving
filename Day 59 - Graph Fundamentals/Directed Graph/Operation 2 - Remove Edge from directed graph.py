def remove_directed_edge(graph, node1,node2):
    if node1 not in graph or node2 not in graph:
        print("Vertex does not exists .")
        return
    if node2 not in graph[node1]:
        print("Edge does not exists .")
        return
    graph[node1].remove(node2)
    print("Edge removed succesfully .")

directed_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
remove_directed_edge(directed_graph, 'A', 'B')
remove_directed_edge(directed_graph, 'X', 'B')
remove_directed_edge(directed_graph, 'A', 'D')
print(directed_graph)