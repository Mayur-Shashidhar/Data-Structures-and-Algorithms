# Binary Tree Maximum Path Sum
- A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
- The path sum of a path is the sum of the node's values in the path.
- Given the root of a binary tree, return the maximum path sum of any non-empty path.

---

## Approach
- Use DFS.
- For every node:
    - Find the maximum path sum from the left subtree.
    - Find the maximum path sum from the right subtree.
- Ignore negative path sums by treating them as 0.
- Calculate the maximum path passing through the current node: left + node.val + right
- Update the global maximum.
- Return to the parent: node.val + max(left, right) because a parent can continue the path through only one child.


### Complexity
- Time : O(n)
- Space : O(h)

---
