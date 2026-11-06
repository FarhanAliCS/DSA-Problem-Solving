### Day 58 — Heaps & Priority Queue

# Topics Covered

- Heap Data Structure
- Min Heap
- Max Heap
- Complete Binary Tree
- Heap Properties
- Python "heapq" Module
- Sift Up and Sift Down
- Priority Queue
- K Largest Elements
- K Smallest Elements
- Kth Largest Element
- Kth Smallest Element

# Heap Types

Min Heap

The smallest element is always at the root.

# Max Heap

The largest element is always at the root.

Python's "heapq" implements a Min Heap by default. A Max Heap can be simulated using negative values.

# Important heapq Functions

Function| Purpose| Complexity
"heapify()"| Convert list into heap| O(n)
"heappush()"| Insert an element| O(log n)
"heappop()"| Remove smallest element| O(log n)
Access "heap[0]"| Get smallest element| O(1)

## Priority Queue

A Priority Queue removes elements according to priority rather than insertion order.

# Python example:

heapq.heappush(queue, (priority, task))

# Problems Practiced

1. Create a Min Heap.
2. Insert an element into a heap.
3. Remove the smallest element.
4. Simulate a Max Heap.
5. Implement a Priority Queue.
6. Find K Largest Elements.
7. Find K Smallest Elements.
8. Find Kth Largest Element.
9. Find Kth Smallest Element.

# Key Concepts Learned

- Heap operations and their time complexities.
- Using negative values to simulate Max Heap.
- Using tuples for priority-based processing.
- Extracting elements in priority order.
- Applying heaps to selection problems.

Status

Day 58 completed successfully.

Next: Day 59 — Graph Fundamentals
    
