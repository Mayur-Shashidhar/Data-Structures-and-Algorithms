# Diameter of Binary Tree
- Given the root of a binary tree, return the length of the diameter of the tree.
- The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
- The length of a path between two nodes is represented by the number of edges between them.

---

## Approach
- Use DFS.
- For every node:
    - Find left subtree height.
    - Find right subtree height.
- Calculate: left_height + right_height
- Update global diameter.
- Return: 1 + max(left_height, right_height) because parent needs height.


### Complexity
- Time : O(n)
- Space : O(h)

---
