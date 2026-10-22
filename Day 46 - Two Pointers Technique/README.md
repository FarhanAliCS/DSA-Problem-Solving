 ### Day 46 — Two Pointers Technique

# Topics Covered

- Two Pointers technique
- Pair sum in a sorted list
- Finding all unique pairs
- Skipping duplicate values
- Finding the closest pair to a target
- Three Sum problem
- Three Sum Closest problem

 # Problems Practiced

1. Check whether a pair exists whose sum equals a target.
2. Find all unique pairs whose sum equals a target.
3. Find the pair whose sum is closest to a target.
4. Find all unique triplets whose sum equals a target.
5. Find the sum of three numbers closest to a target.

# Important Concepts

- Initialize "left = 0" and "right = len(numbers) - 1".
- Use "while left < right" to process two distinct positions.
- Move "left" when the sum is too small.
- Move "right" when the sum is too large.
- Skip repeated values to avoid duplicate pairs and triplets.
- Combine a "for" loop with Two Pointers for Three Sum problems.
- Sorted input is essential for these pointer movements.

# Time Complexity

- Pair Sum: O(n)
- Unique Pairs: O(n)
- Closest Pair: O(n)
- Three Sum: O(n²)
- Three Sum Closest: O(n²)

# What I Learned

I learned how to use the Two Pointers technique on sorted lists, avoid duplicate results, and solve pair and triplet problems more efficiently without using nested loops for every element combination.

Next Step

Continue with Day 47 of the Python DSA roadmap: Sliding Window Technique.