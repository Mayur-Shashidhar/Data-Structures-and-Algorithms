# Subtree of Another Tree
- Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
- A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

---

## Approach
- Create a helper function sameTree(p, q).
- sameTree checks whether two trees are identical.
- For every node in root:
    - Check if current subtree equals subRoot.
    - If yes, return True.
- Otherwise recursively search:
    - Left subtree.
    - Right subtree.
- If no match is found, return False.


### Comlexity
- Time : O(n * m)
- Space : O(h)

---
