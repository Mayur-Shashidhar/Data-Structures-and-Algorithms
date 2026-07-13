# Subsets II
- Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
- The solution set must not contain duplicate subsets. Return the solution in any order.

---

## Approach
- Sort the array.
- Store current subset.
- Loop through remaining elements.
- If current element is same as previous and it's not the first choice at this level: Skip it.
- Otherwise:
    - Choose
    - Recurse
    - Undo


### Complexity
- Time : O(n × 2ⁿ)
- Space : O(n)

---
