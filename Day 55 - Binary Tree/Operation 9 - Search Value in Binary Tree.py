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
def search_value(node , target):
    if node is None:
        return False
    if node.data == target:
        return True
    return search_value(node.left ,target) or search_value(node.right ,target)
    


root=binary_tree()
print(search_value(root , 100))