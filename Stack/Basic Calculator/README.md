# Basic Calculator
- Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
- Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

---

## Approach
- Initialize:
    - result = 0
    - number = 0
    - sign = 1
- Create an empty stack.
- Traverse the string character by character.
- If the character is a digit: Build the complete number.
- If the character is '+' or '-':
    - Add the previous number to the result using the current sign.
    - Update the sign.
    - Reset the number.
- If the character is '(':
    - Push the current result onto the stack.
    - Push the current sign onto the stack.
    - Reset result and sign for the new expression.
- If the character is ')':
    - Finish the current number.
    - Multiply the result by the sign before '('.
    - Add the result before '('.
- After traversal, add any remaining number.
- Return the final result.


### Complexity
- Time : O(n)
- Space : O(n)

---
