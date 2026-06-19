# Permutation in String
- Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
- In other words, return true if one of s1's permutations is the substring of s2.

---

## Approach
- Build a frequency map for s1.
- Create a sliding window of size: len(s1) inside s2.
- Maintain frequency counts for the current window.
- As the window moves:
    - Add the new character entering the window.
    - Remove the old character leaving the window.
- After each move:
    - Compare the window frequency with the frequency of s1.
- If they match:
    - A permutation exists.
    - Return True.
- If all windows are checked and none match: Return False.


### Complexity
- Time : O(n)
- Space : O(1)

---
