# Valid Parentheses
- Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.

---

## Approach
- Create an empty stack.
- Traverse the string character by character.
- If the current character is an opening bracket:
    - Push it onto the stack.
- If the current character is a closing bracket:
    - Check whether the stack is empty.
    - If it is empty, return False.
    - Otherwise pop the top element.
- Verify that the popped opening bracket matches the current closing bracket.
- If they do not match, return False.
- After processing all characters, check whether the stack is empty.
- If the stack is empty, return True.
- Otherwise return False.


### Complexity
- Time : O(n)
- Space : O(n)

---
