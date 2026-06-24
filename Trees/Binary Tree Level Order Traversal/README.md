# Binary Tree Level Order Traversal
- Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

---

## Approach
- Put root in queue.
- While queue is not empty:
    - Get current level size.
    - Process exactly those nodes.
    - Add their children to queue.
- Store current level.
- Return all levels.


### Complexity
- Time : O(n)
- Space : O(n)

---
