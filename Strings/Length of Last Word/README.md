# Length of Last Word
- Given a string s consisting of words and spaces, return the length of the last word in the string.
- A word is a maximal substring consisting of non-space characters only.

---

## Approach (Brute Force)
- Remove extra spaces automatically using split().
- Store all words in a list.
- Take the last word.
- Return its length.


### Complexity
- Time : O(n)
- Space : O(n)

---

## Approach (Optimal)
- Start from the last character.
- Skip all trailing spaces.
- Count characters until a space is found.
- Return the count.


### Complexity
- Time : O(n)
- Space : O(1)

---
