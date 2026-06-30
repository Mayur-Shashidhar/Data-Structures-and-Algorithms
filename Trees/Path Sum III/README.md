# Path Sum III
- Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
- The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

---

## Approach
- Use DFS.
- Maintain:
    - Current prefix sum.
    - Hash map of prefix sums.
- At every node:
    - Add node value to current sum.
    - Check if currentSum - targetSum exists.
    - Add its frequency to the answer.
- Store the current prefix sum.
- Recurse on left and right.
- Remove the current prefix sum before returning (Backtracking).


### Complexity
- Time : O(n)
- Space : O(n)

---
