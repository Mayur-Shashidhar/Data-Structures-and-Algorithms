# Longest Substring Without Repeating Characters
- Given a string s, find the length of the longest substring without duplicate characters.

---

## Approach
- Maintain a window using two pointers:
    - Left
    - Right
- Expand the window by moving the right pointer.
- Store characters currently inside the window in a HashSet.
- If the new character is not present:
    - Add it to the set.
    - Update the maximum length.
- If the new character already exists:
    - Shrink the window from the left.
    - Remove characters until the duplicate disappears.
- Continue until the string ends.


### Complexity
- Time : O(n)
- Space : O(1)

---
