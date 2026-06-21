# Evaluate Reverse Polish Notation
- You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
- Evaluate the expression. Return an integer that represents the value of the expression.
- Note that:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.

---

## Approach
- Create an empty stack.
- Traverse each token in the expression.
- If the token is a number:
    - Push it onto the stack.
- If the token is an operator:
    - Pop the top two numbers from the stack.
    - Apply the operation.
    - Push the result back onto the stack.
- Continue until all tokens are processed.
- The final element in the stack is the answer.
- Return that value.


### Complexity
- Time : O(n)
- Space : O(n)

---
