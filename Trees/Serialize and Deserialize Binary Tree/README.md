# Serialize and Deserialize Binary Tree
- Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
- Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
- Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

---

## Serialize Approach
- Use preorder DFS.
- If node is None: Add "N".
- Otherwise:
    - Add node value.
    - Serialize left subtree.
    - Serialize right subtree.
- Join everything with commas.


## Deserialize Approach
- Split the string into a list.
- Read values one by one.
- If value is "N": Return None.
- Otherwise:
    - Create a node.
    - Build left subtree.
    - Build right subtree.
- Return the reconstructed tree.


### Complexity
- Time : O(n)
- Space : O(n)

---
