# Reverse Words in a String
- Given an input string s, reverse the order of the words.
- A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
- Return a string of the words in reverse order concatenated by a single space.
- Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

---

## Approach
- Split the string into words.
    - This automatically removes leading, trailing, and extra spaces.
- Reverse the list of words.
- Join the words using a single space.
- Return the resulting string.


### Complexity
- Time : O(n)
- Space : O(n)

---
