# Palindromic Substrings
- Given a string s, return the number of palindromic substrings in it.
- A string is a palindrome when it reads the same backward as forward.
- A substring is a contiguous sequence of characters within the string.

---

## Approach
- Initialize a counter.
- For every index:
    - Expand around it as an odd-length center.
    - Expand around it as an even-length center.
- Every time characters match:
    - A new palindrome is found.
    - Increase the count.
- Continue expanding until characters no longer match.
- Return the total count.


### Complexity
- Time : O(n²)
- Space : O(1)

---
