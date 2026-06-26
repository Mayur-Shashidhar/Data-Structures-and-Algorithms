# Validate Binary Search Tree
- Given the root of a binary tree, determine if it is a valid binary search tree (BST).
- A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys strictly less than the node's key.
    - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

---

## Approach
- Start DFS from the root with range (-∞, +∞).
- If node is None, return True.
- If node value is not within (low, high), return False.
- Recursively check:
    - Left subtree with (low, node.val)
    - Right subtree with (node.val, high)
- Return True only if both subtrees are valid.


### Complexity
- Time : O(n)
- Space : O(h)

---
