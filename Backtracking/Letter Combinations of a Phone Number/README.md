# Letter Combinations of a Phone Number
- Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
- A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

---

## Approach
- Create a digit → letters mapping.
- Start from index 0.
- For every letter of the current digit:
    - Choose the letter.
    - Recurse to the next digit.
    - Undo.
- When all digits are processed: Store the current string.


### Complexity
- Time : O(4ⁿ × n)
- Space : O(n)

---
