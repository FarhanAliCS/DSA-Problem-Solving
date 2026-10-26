# Day 48 — Prefix Sum in Python

# Topics Covered

- Understanding the Prefix Sum technique
- Building a Prefix Sum array
- Calculating the sum of a range using Prefix Sum
- Answering multiple range-sum queries
- Finding the Equilibrium Index
- Finding the Pivot Index
- Validating query indexes
- Handling invalid queries using "None" and "continue"
- Understanding time and space complexity

# Key Concepts

Prefix Sum stores cumulative sums so that range sums can be calculated efficiently.

# Range Sum Formula:

If "left > 0":

"range_sum = prefix[right] - prefix[left - 1]"

# If "left == 0":

"range_sum = prefix[right]"

# Equilibrium / Pivot Index:

The sum of elements to the left equals the sum of elements to the right, excluding the current element.

"right_sum = total_sum - left_sum - numbers[i]"

# Complexity

- Building the prefix array: O(n)
- Answering each range query: O(1)
- Answering q queries after preprocessing: O(n + q)

# Practice Summary

Completed prefix-sum construction, range-sum calculations, multiple queries, equilibrium/pivot index problems, and invalid-query handling.

Status

Day 48 Completed ✅

Next: Day 49 — Continue the Python DSA roadmap.