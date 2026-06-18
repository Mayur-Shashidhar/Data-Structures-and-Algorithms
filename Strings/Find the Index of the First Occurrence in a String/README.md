# Find the Index of the First Occurrence in a String
- Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

---

# Approach
- Start from the first position of haystack.
- At every position, try to match the entire needle.
- Compare characters one by one.
- If all characters match:
    - Return the current starting index.
- If a mismatch occurs:
    - Move to the next position in haystack.
- Continue until all possible starting positions have been checked.
- f no match is found:
    - Return -1.


### Complexity
- Time : O(n × m)
- Space : O(1)

---
