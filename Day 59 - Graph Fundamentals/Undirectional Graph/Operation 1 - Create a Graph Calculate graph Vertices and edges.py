# Write a program that:
# Creates the graph using a dictionary.
# Prints the complete graph.
# Prints all neighbors of vertex "A".
# Prints all neighbors of vertex "D".
# Prints the total number of vertices .
# Print number of edges.
def number_of_edges(graph):
    total=0
    for node in graph:
        total+=len(graph[node])
    return total//2
graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E'],
    'D':['B','E'],
    'E':['C','D']
}
print(graph)
print("Neighbors 'A'",graph['A'])
print("Neighbors 'D':",graph['D'])
print("Number of vertices :",len(graph))
print("Number of edges :",number_of_edges(graph))

