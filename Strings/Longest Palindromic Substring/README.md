# Longest Palindromic Substring
- Given a string s, return the longest palindromic substring in s.

---

## Approach
- Treat every index as the center of a palindrome.
- Expand outward while characters match.
- Calculate the palindrome length.
- Repeat for:
    - Odd-length palindrome
    - Even-length palindrome
- Keep track of the longest palindrome found.
- Return the longest substring.


### Complexity
- Time : O(n²)
- Space : O(1)

---
