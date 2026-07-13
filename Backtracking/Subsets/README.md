# Subsets
- Given an integer array nums of unique elements, return all possible subsets (the power set).
- The solution set must not contain duplicate subsets. Return the solution in any order.

---

## Approach
- Start with empty subset.
- Store current subset.
- For every remaining number:
    - Choose it.
    - Recurse.
    - Undo.
- Return all subsets.


### Complexity
- Time : O(n × 2ⁿ)
- Space : O(n)

---
