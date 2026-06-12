# Group Anagrams
- Given an array of strings strs, group the anagrams together. You can return the answer in any order.

---

## Approach
- Create a HashMap.
- For every word:
    - Sort the word.
    - Use the sorted word as the key.
- Store all words with the same key together.
- Return all groups.


### Complexity
- Time : O(n × k log k)
- Space : O(n × k)

---
