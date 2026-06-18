# Is Subsequence
- Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
- A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

---

## Approach
- Place one pointer at the beginning of s.
- Place another pointer at the beginning of t.
- Traverse through t.
- Whenever the characters at both pointers are the same:
    - Move the pointer in s.
    - Move the pointer in t.
- If the characters are different:
    - Move only the pointer in t.
    - Continue until the end of t is reached.
- If the pointer in s reaches the end:
    - All characters of s were found in order.
    - Return True.
- Otherwise:
    - Return False.


### Complexity
- Time : O(n)
- Space : O(1)

---
