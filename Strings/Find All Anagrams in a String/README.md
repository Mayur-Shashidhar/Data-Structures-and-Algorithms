# Find All Anagrams in a String
- Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

---

## Approach
- Build a frequency map for p.
- Create a sliding window of size len(p).
- Maintain the frequency map of the current window.
- As the window moves:
    - Add the new character entering the window.
    - Remove the old character leaving the window.
- Compare the window frequency map with the pattern frequency map.
- If they match: Store the starting index.
- Continue until the string ends.


### Complexity
- Time : O(n)
- Space : O(1)

---
