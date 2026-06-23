# Maximum Depth of Binary Tree
- Given the root of a binary tree, return its maximum depth.
- A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## Approach
- If node is None, return 0.
- Find depth of left subtree.
- Find depth of right subtree.
- Return: 1 + max(left_depth, right_depth)


### Complexity
- Time : O(n)
- Space : O(h)

---
