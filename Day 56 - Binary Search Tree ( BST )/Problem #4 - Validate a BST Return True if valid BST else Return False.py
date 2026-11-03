class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root , value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left=insert(root.left , value)
    elif value > root.data:
        root.right=insert(root.right , value)

    return root

def is_valid_bst(root , minimum=float("-inf") , maximum=float("inf")):
    if root is None:
        return True
    
    if root.data <= minimum or root.data >= maximum:
        return False
    left=is_valid_bst(root.left , minimum ,root.data)
    right=is_valid_bst(root.right , root.data , maximum)

    return left and right

    


root=None
values=[20,30,40,50,60,70,80]
for value in values:
    root=insert(root , value)

print(is_valid_bst(root))
    
