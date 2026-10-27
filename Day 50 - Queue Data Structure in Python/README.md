### Day 50 — Queue Data Structure in Python

# Overview

Today, I learned about the Queue data structure and practiced its basic operations in Python.

# What I Learned

- Queue follows FIFO (First In, First Out).
- Enqueue: Add an element to the rear.
- Dequeue: Remove and return the first element.
- Peek: View the first element without removing it.
- Check whether a queue is empty.
- Handle empty queues safely.
- Use "collections.deque" for efficient queue operations.

# Queue Using a List

- "append(value)" adds an element.
- "pop(0)" removes and returns the first element.
- "queue[0]" accesses the first element.

Note: Removing the first element using "pop(0)" takes O(n) time.

# Queue Using Deque

from collections import deque

queue = deque()

queue.append(20)
queue.append(30)
queue.append(40)

print("Queue:", queue)

removed = queue.popleft()

print("Removed:", removed)
print("Remaining:", queue)

# Complexity

Operation| List| Deque
Enqueue at rear| O(1) amortized| O(1)
Dequeue from front| O(n)| O(1)
Peek at front| O(1)| O(1)
Check if empty| O(1)| O(1)

# Key Takeaway

A queue processes elements in FIFO order. Python's "collections.deque" is generally the better choice when items are frequently removed from the front.

# Status

Day 50 completed — Queue Data Structure in Python.