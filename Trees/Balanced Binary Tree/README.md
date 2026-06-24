# Balanced Binary Tree
- Given a binary tree, determine if it is height-balanced.

---

## Approach
- If node is None: Return 0.
- Find left subtree height.
- Find right subtree height.
- If: abs(left - right) > 1, the tree is not balanced.
- Return: 1 + max(left, right) to parent.
- If any subtree is unbalanced, propagate that information upward.


### Complexity
- Time : O(n)
- Space : O(h)

---
