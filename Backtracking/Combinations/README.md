# Combinations
- Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
- You may return the answer in any order.

---

## Approach
- Start from number 1.
- Choose a number.
- Recurse on the next number.
- Undo.
- If path size == k: Store it.


### Comlexity
- Time : O(C(n,k) × k)
- Space : O(k)

---
