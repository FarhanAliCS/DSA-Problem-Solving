class Node:
    def __init__(self , data):
        self.data=data
        self.left=None
        self.right=None

def insert(root , value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left=insert(root.left,value)
    elif value > root.data:
        root.right=insert(root.right, value)

    return root

def search(node , target):
    if node is None:
        return False
    if node.data == target:
        return True
    elif target < node.data:
        return search(node.left,target)
    else:
        return search(node.right,target)


root=None
values=[20,30,40,50,60,70,80]
for value in values:
    root=insert(root ,value)

print(search(root , 30))