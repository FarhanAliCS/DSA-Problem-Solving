class Node:
    def __init__(self , data):
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

def count_leaf(node):
    if node is None:
        return 0
    if node.left is None  and node.right is None:
        return 1
    left=count_leaf(node.left)
    right=count_leaf(node.right)

    return  left + right

root=binary_tree()
print(count_leaf(root))
    