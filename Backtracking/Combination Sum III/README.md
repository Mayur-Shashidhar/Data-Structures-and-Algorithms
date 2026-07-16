# Combination Sum III
- Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
    - Only numbers 1 through 9 are used.
    - Each number is used at most once.
- Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

---

## Approach
- Start from 1.
- Choose a number.
- Reduce target.
- Move to the next number.
- Undo.
- Store answer only if:
    - len(path) == k
    - AND target == 0


### Complexity
- Time : O(C(9, k))
- Space : O(k)

---
