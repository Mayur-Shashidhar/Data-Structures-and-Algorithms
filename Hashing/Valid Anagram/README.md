# Valid Anagram
- Given two strings s and t, return true if t is an anagram of s, and false otherwise.

---

## Approach
- If the lengths of the strings are different:
    - Return False.
- Create a HashMap (dictionary).
- Traverse the first string:
    - Increase the count of each character.
- Traverse the second string:
    - Decrease the count of each character.
- After processing both strings:
    - Every character count should be 0.
- If any count is not 0:
    - Return False.
- Otherwise:
    - Return True.


### Complexity
- Time : O(n)
- Space : O(1)

---
