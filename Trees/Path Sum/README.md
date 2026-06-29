# Path Sum
- Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
- A leaf is a node with no children.

---

## Approach
- If the node is None: Return False.
- If the current node is a leaf: Check if its value equals the remaining target sum.
- Recursively search:
    - Left subtree with targetSum - node.val.
    - Right subtree with targetSum - node.val.
- If either subtree returns True: Return True.
- Otherwise return False.


### Complexity
- Time : O(n)
- Space : O(h)

---
