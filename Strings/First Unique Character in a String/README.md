# First Unique Character in a String
- Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

---

## Approach
- Traverse the string and count the frequency of every character.
- Store the frequencies in a HashMap.
- Traverse the string again from left to right.
- For each character:
    - Check if its frequency is 1.
- The first character whose frequency is 1 is the answer.
- Return its index.
- If no character has frequency 1, return -1.


### Complexity
- Time : O(n)
- Space : O(1)

---
