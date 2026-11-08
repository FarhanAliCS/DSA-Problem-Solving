### Day 60 — Graph Traversal (BFS & DFS)

# Overview

Today I learned how to traverse graphs using Breadth-First Search (BFS) and Depth-First Search (DFS).

## Topics Covered

# 1. Breadth-First Search (BFS)

- BFS visits vertices level by level.
- Uses a Queue (FIFO).
- Implemented BFS using Python's "collections.deque".
- Used a visited set to prevent repeated visits.
- Implemented BFS for disconnected graphs.

# 2. Depth-First Search (DFS)

- DFS explores one path as deeply as possible before backtracking.
- Uses a Stack (LIFO) or recursion.
- Implemented iterative DFS using a list as a stack.
- Implemented recursive DFS.
- Implemented DFS for disconnected graphs.

# 3. BFS vs DFS

Feature| BFS| DFS
Traversal| Level by level| Deep path first
Data structure| Queue| Stack
Implementation| Iterative| Iterative or recursive
Time complexity| O(V + E)| O(V + E)
Space complexity| O(V)| O(V)

# 4. Important Python Concepts

- "collections.deque"
- "append()"
- "popleft()"
- "pop()"
- Recursion
- Sets and visited tracking
- Graph adjacency lists

## Complexity Analysis

For an adjacency-list graph:

- BFS: O(V + E) time, O(V) space.
- DFS: O(V + E) time, O(V) space.

Where:

- V = Number of vertices
- E = Number of edges

# What I Learned

- How BFS and DFS work.
- How to use queues and stacks for graph traversal.
- How recursion works in DFS.
- How to traverse disconnected graphs.
- Why a visited set is important.
- How to analyze graph traversal complexity.

Day 60 Status

Completed

Next

Day 61 — DSA Revision + Problem-Solving Challenge.