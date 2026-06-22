# Remove K Digits
- Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

---

## Approach
- Create an empty stack.
- Traverse each digit in the number.
- While:
    - The stack is not empty.
    - k > 0.
    - Current digit is smaller than the top of the stack. Pop the stack and decrease k.
- Push the current digit into the stack.
- After traversal, if k is still greater than 0: Remove digits from the end of the stack.
- Build the final number from the stack.
- Remove leading zeros.
- If the result becomes empty, return "0".
- Otherwise return the resulting string.


### Complexity
- Time : O(n)
- Space : O(n)

---
