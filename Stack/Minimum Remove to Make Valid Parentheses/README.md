# Minimum Remove to Make Valid Parentheses
- Given a string s of '(' , ')' and lowercase English characters.
- Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
- Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.

---

## Approach
- Create a stack to store indices of opening parentheses.
- Convert the string into a list so characters can be modified.
- Traverse the string.
- If the character is '(':
    - Push its index into the stack.
- If the character is ')':
    - If the stack is not empty:
        - Pop a matching '(' index.
    - Otherwise:
        - Mark this ')' for removal.
- After traversal, any indices left in the stack correspond to unmatched '('.
- Mark all those '(' for removal.
- Build the final string by skipping marked characters.
- Return the resulting string.


### Complexity
- Time : O(n)
- Space : O(n)

---
