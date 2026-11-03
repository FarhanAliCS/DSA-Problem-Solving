from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def tree():
    root=Node(10)
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.left=Node(60)
    root.right.right=Node(70)
    return root

def zigzag_traversal(root):
    if root is None:
        return []
    queue=deque([root])
    result=[]
    left_to_right=True
    while queue:
        level_len=len(queue)

        current_level=[]
        for _ in range(level_len):
            current=queue.popleft()
            current_level.append(current.data)
    
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        if not left_to_right:
            current_level.reverse()
        result.append(current_level)
        left_to_right=not left_to_right

        
    return result

root=tree()
print(zigzag_traversal(root))