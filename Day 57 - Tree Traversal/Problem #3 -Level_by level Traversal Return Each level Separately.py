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

def level_order_by_level(root):
    if root is None:
        return []
    queue=deque([root])
    result=[]
    
    while queue:
        level_size=len(queue)
        current_level=[]
        for _ in range(level_size):
            current=queue.popleft()
            current_level.append(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        result.append(current_level)

    return result

root=tree()
print(level_order_by_level(root))