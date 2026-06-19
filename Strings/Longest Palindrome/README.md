# Longest Palindrome
- Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
- Letters are case sensitive, for example, "Aa" is not considered a palindrome.

---

## Approach
- Count the frequency of every character.
- Traverse all frequencies.
- If a frequency is even: Add the entire frequency to the answer.
- If a frequency is odd: Add the largest even part. (count - 1)
- Remember if any odd frequency exists.
- After processing all frequencies: Add 1 for the center character if an odd frequency was found.
- Return the total length.


### Complexity
- Time : O(n)
- Space : O(1)

---
