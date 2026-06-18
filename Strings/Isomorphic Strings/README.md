# Isomorphic Strings
- Given two strings s and t, determine if they are isomorphic.
- Two strings s and t are isomorphic if the characters in s can be replaced to get t.
- All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

---

## Approach
- Create two HashMaps.
- First HashMap stores: character in s → character in t
- Second HashMap stores: character in t → character in s
- Traverse both strings together.
- For each pair of characters:
    - Check if an existing mapping is violated.
    - Check if reverse mapping is violated.
- If any violation occurs:
    - Return False.
    - Otherwise store the mappings.
- If the entire traversal completes: Return True.


### Complexity
- Time : O(n)
- Space : O(n)

---
