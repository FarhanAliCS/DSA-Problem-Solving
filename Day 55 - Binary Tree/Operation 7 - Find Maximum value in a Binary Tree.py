class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def binary_tree():
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.left=Node(60)
    root.right.right=Node(70)
    return root

def maximum_value(node):
    if node is None:
        return float("-inf")
    
    left=maximum_value(node.left)
    right=maximum_value(node.right)
    maximum=max(node.data,left,right)

    return maximum

root=binary_tree()
print(maximum_value(root))