# Invert Binary Tree
- Given the root of a binary tree, invert the tree, and return its root.

---

## Approach
- If the current node is null: Return null.
- Swap the left and right child of the current node.
- Recursively invert the left subtree.
- Recursively invert the right subtree.
- Return the root.


### Complexity
- Time : O(n)
- Space : O(h)

---
