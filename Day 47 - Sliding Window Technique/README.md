## Day 47 - Sliding Window Technique

# Topics Learned

- Sliding Window Technique
- Fixed-Size Sliding Window
- Variable-Size Sliding Window
- Two Pointers with Sliding Window
- Time and Space Complexity

# Problems Solved

1. Find the maximum sum of a fixed-size window.
2. Find the minimum sum of a fixed-size window.
3. Find the starting index of the maximum-sum window.
4. Count windows whose sum is greater than a target.
5. Find the longest subarray with sum at most a target.
6. Find the minimum subarray length with sum at least a target.

# Key Concepts

- Use "left" and "right" pointers to manage a window.
- Expand the window by moving "right".
- Shrink the window by moving "left" when necessary.
- Update the current sum instead of recalculating it from scratch.
- Use "right - left + 1" to calculate the window length.
- Sliding Window can solve many contiguous subarray problems efficiently.

# Complexity

- Time Complexity: O(n) for the practiced Sliding Window algorithms.
- Auxiliary Space Complexity: O(1), excluding temporary slices and input storage.

# Important Note

The variable-size Sliding Window problems practiced today assume positive integers. Negative numbers can require different techniques.

Day 47 Status

Completed

Next Day

Day 48 - Prefix Sum