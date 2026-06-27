# Construct Binary Tree from Preorder and Inorder Traversal
- Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

---

## Approach
- Create a hash map that stores each value's index in the inorder array.
- Maintain a pointer (preIndex) to the current root in the preorder array.
- Recursively build the tree:
    - If the inorder range is invalid (left > right), return None.
    - Pick preorder[preIndex] as the root and increment preIndex.
    - Find the root's index in the inorder array using the hash map.
    - Recursively build the left subtree using the left part of the inorder range.
    - Recursively build the right subtree using the right part.
- Return the constructed root.


### Complexity
- Time : O(n)
- Space : O(n)

---
