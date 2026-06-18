# Longest Common Prefix
- Write a function to find the longest common prefix string amongst an array of strings.
- If there is no common prefix, return an empty string "".

---

## Approach
- Take the first string.
- Traverse each character of the first string.
- For every character position:
    - Compare that character with the same position in all other strings.
- If:
    - A string ends, or
    - Characters differ
    - then return everything before that position.
- If all positions match, return the entire first string.


### Complexity
- Time : O(n × m)
- Space : O(1)

---
