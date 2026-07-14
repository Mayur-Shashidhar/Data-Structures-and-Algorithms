# Combination Sum II
- Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
- Each number in candidates may only be used once in the combination.
- Note: The solution set must not contain duplicate combinations.

---

## Approach
- Sort the array.
- If target == 0: Store answer.
- If target < 0: Return.
- Loop through candidates.
- Skip duplicates.
- Choose current number.
- Recurse using i + 1.
- Undo.


### Complexity
- Time : O(2ⁿ)
- Space : O(n)

---
