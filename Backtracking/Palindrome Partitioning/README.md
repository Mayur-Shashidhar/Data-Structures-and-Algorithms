# Palindrome Partitioning
- Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

---

## Approach
- Start from index 0.
- Try every possible substring.
- If substring is a palindrome:
    - Choose it.
    - Recurse from the next index.
    - Undo.
- Ignore non-palindrome substrings.
- When start reaches the end: Store the partition.


### Complexity
- Time : O(n × 2ⁿ)
- Space : O(n)

---
