# Binary Tree Zigzag Level Order Traversal
- Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

---

## Approach
- If the tree is empty, return an empty list.
- Create a queue and add the root.
- Maintain a boolean leftToRight.
- While the queue is not empty:
    - Find the number of nodes in the current level.
    - Process all nodes in that level.
    - Add their children to the queue.
    - If leftToRight is True: Store the level normally.
    - Otherwise: Reverse the level.
- Toggle leftToRight.
- Return the result.


### Complexity
- Time : O(n)
- Space : O(n)

---
