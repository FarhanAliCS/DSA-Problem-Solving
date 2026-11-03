### Day 57 — Tree Traversal

# Topics Covered

- Tree Traversal Revision
- Breadth-First Search (BFS)
- Level Order Traversal
- Level-by-Level Traversal
- Maximum Value at Each Level
- Sum at Each Level
- Average at Each Level
- Zigzag Level Order Traversal

## Traversal Types

# 1. Depth-First Search (DFS)

- Preorder: Root → Left → Right
- Inorder: Left → Root → Right
- Postorder: Left → Right → Root

# 2. Breadth-First Search (BFS)

- Visits nodes level by level.
- Uses a queue.
- Implemented using Python's "deque".

Zigzag Traversal

Visits alternate levels in opposite directions.

# Example:

[
    [10],
    [30, 20],
    [40, 50, 60, 70]
]

# Key Concepts Learned

- Using "deque" for efficient queue operations.
- Processing one tree level at a time.
- Using "len(queue)" to track the current level.
- Reversing alternate levels.
- Handling an empty tree.

Complexity

# For BFS and its level-order variations:

- Time Complexity: O(n)
- Auxiliary Queue Space: O(w), where w is the maximum tree width.
- Result storage: O(n) when storing all node values.

Status

Day 57 completed successfully.

Next: Day 58 — Heaps & Priority Queue