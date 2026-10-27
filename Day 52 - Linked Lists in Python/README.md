### Day 52 — Linked Lists in Python

# Overview

Today, I learned the fundamentals of singly linked lists and practiced creating, connecting, traversing, and counting nodes.

# Topics Covered

- What a linked list is
- Nodes and their data
- The "next" reference
- Connecting nodes manually
- Building a linked list dynamically
- Traversing a linked list
- Counting nodes
- Handling invalid user input

# Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Building a Linked List

I implemented a function that accepts user input, creates nodes dynamically, connects them using "head" and "tail", and stops when the user enters "done".

# Counting Nodes

I implemented "count_nodes(head)" by traversing the linked list and incrementing a counter for every node.

# Complexity

Operation| Time Complexity
Build a linked list using a tail reference| O(n)
Traverse the linked list| O(n)
Count nodes| O(n)

Space complexity for storing n nodes: O(n).

# Key Takeaway

A singly linked list consists of nodes connected through references. The "head" provides access to the list, while a "tail" reference makes appending nodes efficient.

Status

Day 52 completed — Linked Lists in Python.