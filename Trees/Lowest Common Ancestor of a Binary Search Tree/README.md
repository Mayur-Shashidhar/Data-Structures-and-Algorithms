# Lowest Common Ancestor of a Binary Search Tree
- Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
- According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---

## Approach
- Start from root.
- If both p and q are smaller: Move left.
- If both p and q are larger: Move right.
- Otherwise: Current node is the LCA.
- Return it.


### Complexity
- Time : O(h)
- Space : O(1)

---
