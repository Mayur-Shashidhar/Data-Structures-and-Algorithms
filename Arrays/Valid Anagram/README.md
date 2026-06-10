# Valid Anagram
- Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
- An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

---

## Approach
- If the two strings have different lengths, return false immediately.
- Create two hash maps to store character frequencies for each string.
- Iterate through both strings at the same time:
    - Increase the character count for s[i] in the first map.
    - Increase the character count for t[i] in the second map.
- After building both maps, compare them:
    - If the maps are equal, return true.
- Otherwise, return false.


### Complexity
- Time : O(n+m)
- Space : O(1)

---
