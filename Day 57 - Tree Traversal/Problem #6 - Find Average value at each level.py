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

def average_at_each_level(root):
    if root is None:
        return []
    queue=deque([root])
    result=[]
    while queue:
        level_len=len(queue)
        total=0
        for _ in range(level_len):
            current=queue.popleft()
            total+=current.data
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        average=total/level_len
        result.append(average)
        
    return result

root=tree()
print(average_at_each_level(root))