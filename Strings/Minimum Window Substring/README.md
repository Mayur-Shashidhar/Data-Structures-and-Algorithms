# Minimum Window Substring
- Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
- The testcases will be generated such that the answer is unique.

---

## Approach
- Count the frequency of every character in t.
- Create a sliding window using two pointers:
    - Left
    - Right
- Expand the window by moving the right pointer.
    - As characters enter the window:
- Update their frequencies.
- Keep track of how many required characters have been matched.
- Once all required characters are present:
    - The window becomes valid.
- Now try shrinking the window from the left:
    - Remove unnecessary characters.
    - Update the minimum window length whenever a smaller valid window is found.
- If removing a character makes the window invalid:
    - Stop shrinking.
    - Continue expanding from the right.
- Repeat until the entire string has been processed.
- Return the smallest valid window found.


### Complexity
- Time : O(n)
- Space : O(m)

---
