class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,value):
    if root is None:
        return Node(value)
    
    if value < root.data:
        root.left=insert(root.left , value)
    elif value > root.data:
        root.right=insert(root.right , value)
    return root


def inorder_treversel(node):
    if node is None:
        return None
    inorder_treversel(node.left)
    print(node.data)
    inorder_treversel(node.right)

root=None
values=[20,30,40,50,60,70,80]
for value in values:
    root=insert(root,value)

inorder_treversel(root)
