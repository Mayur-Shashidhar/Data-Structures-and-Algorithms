# Kth Smallest Element in a BST
- Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

---

## Approach
- Initialize a counter count = 0.
- Perform an inorder DFS:
    - Traverse the left subtree.
    - Increment count.
    - If count == k, return the current node's value.
    - Traverse the right subtree.
- Stop searching once the answer is found.


### Complexity
- Time : O(h + k)
- Space : O(h)

---
