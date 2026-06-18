# Word Pattern
- Given a pattern and a string s, find if s follows the same pattern.
- Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
    - Each letter in pattern maps to exactly one unique word in s.
    - Each unique word in s maps to exactly one letter in pattern.
    - No two letters map to the same word, and no two words map to the same letter.

 ---

 ## Approach
- Split the string into words.
- If the number of words is not equal to the length of the pattern:
    - Return False.
- Create two HashMaps.
- Store: pattern character → word and word → pattern character
- Traverse both together.
- For each pair:
    - Check whether existing mappings are violated.
    - If yes, return False.
- Otherwise store the mappings.
- If traversal finishes successfully: Return True.


### Complexity
- Time : O(n)
- Space : O(n)

---
