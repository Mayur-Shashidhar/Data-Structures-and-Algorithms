# Generate Parentheses
- Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

## Approach
- Use backtracking to build the string character by character.
- Maintain:
    - Number of opening brackets used.
    - Number of closing brackets used.
- If the length of the current string becomes 2 * n:
    - Add it to the answer.
- If opening brackets used are less than n:
    - Add '(' and continue.
- If closing brackets used are less than opening brackets used:
    - Add ')' and continue.
- Explore all valid possibilities.
- Return the answer list.


### Complexity
- Time : O(4^n/√n)
- Space : O(n)

---
