# Lowest Common Ancestor of a Binary Tree
- Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
- According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---

## Approach
- If the current node is None, return None.
- If the current node is p or q, return the current node.
- Recursively search the left subtree.
- Recursively search the right subtree.
- If both left and right are not None, return the current node.
- Otherwise, return whichever of left or right is not None.


### Complexity
- Time : O(n)
- Space : O(h)

---
