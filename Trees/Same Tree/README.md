# Same Tree
- Given the roots of two binary trees p and q, write a function to check if they are the same or not.
- Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

---

## Approach
- If both nodes are None: Return True.
- If one node is None and the other isn't: Return False.
- If values are different: Return False.
- Recursively compare:
    - Left subtrees.
    - Right subtrees.
- Return True only if both comparisons are True.


### Complexity
- Time : O(n)
- Space : O(h)

---
