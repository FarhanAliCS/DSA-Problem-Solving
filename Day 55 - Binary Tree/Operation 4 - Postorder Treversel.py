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

def postorder_treversel(node):
    if node is None:
        return 
    left=postorder_treversel(node.left)
    right=postorder_treversel(node.right) 
    print(node.data)

    


root=binary_tree()
postorder_treversel(root)