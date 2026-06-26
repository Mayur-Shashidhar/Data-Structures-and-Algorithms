# Count Good Nodes in Binary Tree
- Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
- Return the number of good nodes in the binary tree.

---

## Approach
- If node is None, return 0.
- Compare current value with maximum so far.
- If current node is good:
    - count = 1
   - else count = 0.
- Update maximum value.
- Return: count + left subtree + right subtree.


### Complexity
- Time : O(n)
- Space : O(h)

---
