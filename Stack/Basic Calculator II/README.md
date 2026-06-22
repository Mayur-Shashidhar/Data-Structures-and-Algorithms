# Basic Calculator II
- Given a string s which represents an expression, evaluate this expression and return its value. 
- The integer division should truncate toward zero.
- You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
- Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

---

## Approach
- Create an empty stack.
- Traverse the string character by character.
- Build numbers digit by digit.
- Whenever an operator or the end of the string is reached:
    - Process the previous operator.
- If the previous operator is:
    - '+' → Push the number.
    - '-' → Push the negative number.
    - '*' → Pop, multiply, push result.
    - '/' → Pop, divide, push result.
- Update the current operator.
- Reset the current number.
- After traversal, sum all values in the stack.
- Return the result.


### Complexity
- Time : O(n)
- Space : O(n)

---
