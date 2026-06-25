# Binary Tree Right Side View
- You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

---

## Approach
- If the tree is empty, return an empty list.
- Create a queue and add the root.
- While the queue is not empty:
    - Find the number of nodes in the current level.
    - Process each node in that level.
    - Add its left and right children to the queue.
    - If it's the last node of the level, add its value to the answer.
- Return the answer.


### Complexity
- Time : O(n)
- Space : O(n)

---
