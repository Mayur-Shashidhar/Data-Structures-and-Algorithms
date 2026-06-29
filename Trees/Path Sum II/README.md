# Path Sum II
- Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
- A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

---

## Approach
- Use DFS.
- Maintain:
    - Current path.
    - Remaining target sum.
- Add the current node to the path.
- If the current node is a leaf:
    - Check if the remaining target equals the node's value.
    - If yes, add a copy of the path to the answer.
- Recursively explore:
    - Left subtree.
    - Right subtree.
- Remove the current node from the path before returning (Backtracking).
- Return all valid paths.


### Complexity
- Time : O(n)
- Space : O(h)

---
