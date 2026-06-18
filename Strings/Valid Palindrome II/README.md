# Valid Palindrome II
- Given a string s, return true if the s can be palindrome after deleting at most one character from it.

---

## Approach
- Place one pointer at the beginning of the string.
- Place another pointer at the end of the string.
- While the characters at both pointers are equal:
    - Move both pointers inward.
- If a mismatch occurs:
    - Try skipping the left character and check if the remaining substring is a palindrome.
    - Try skipping the right character and check if the remaining substring is a palindrome.
- If either check returns true: Return True.
- Otherwise: Return False.
- If no mismatch occurs during the traversal: Return True.


### Complexity
- Time : O(n)
- Space : O(1)

---
