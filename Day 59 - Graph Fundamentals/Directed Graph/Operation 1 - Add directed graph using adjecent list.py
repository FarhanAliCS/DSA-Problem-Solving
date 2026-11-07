def add_directed_edge(graph, node1, node2):

    if node1 not in graph or node2 not in graph:
        print("Vertex does not exist.")
        return

    if node2 in graph[node1]:
        print("Edge already exists.")
        return

    graph[node1].append(node2)
    print("Directed edge added successfully.")


directed_graph = {
    'A': [],
    'B': [],
    'C': [],
    'D': []
    }

add_directed_edge(directed_graph, 'A', 'B')
add_directed_edge(directed_graph,'A','C')
add_directed_edge(directed_graph,'B','D')
add_directed_edge(directed_graph,'C','D')
add_directed_edge(directed_graph,'D','A')

print("\n",directed_graph)