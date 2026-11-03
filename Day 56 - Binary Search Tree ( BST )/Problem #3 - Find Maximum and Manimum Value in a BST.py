class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left=insert(root.left ,value)
    elif value > root.data:
        root.right=insert(root.right,value)

    return root

def maximum(node):
    if node is None:
        return float("-inf")
    maximum_value=node.data
    maximum_value=max(maximum_value ,maximum(node.right))
    return maximum_value
def minimum(node):
    if node is None:
        return float("inf")
    minimum_value=node.data
    minimum_value=min(minimum_value ,minimum(node.left))
    return minimum_value

root=None
values=[20,30,40,50,60,70,80]
for value in values:
    root=insert(root , value)

print(maximum(root))
print(minimum(root))

        