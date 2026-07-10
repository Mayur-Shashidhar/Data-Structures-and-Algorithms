# Reorganize String
- Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
- Return any possible rearrangement of s or return "" if not possible.

---

## Approach
- Count character frequencies.
- Build a Max Heap.
- Keep a previous character.
- While heap not empty:
    - Pop highest frequency character.
    - Add to answer.
    - Decrease frequency.
    - Push previous character back if it still has occurrences.
    - Update previous.
- If answer length != string length return ""
- Otherwise return answer.


### Complexity
- Time : O(n log k)
- Space : O(k)

---
