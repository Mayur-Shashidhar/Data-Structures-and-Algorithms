# Largest Number
- Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
- Since the result may be very large, so you need to return a string instead of an integer.

---

## Approach
- Convert all numbers into strings.
- Sort them using a custom ordering.
- For two strings a and b:
    - If ab > ba: a should come first.
    - Otherwise: b should come first.
- Join all strings together.
- If the result starts with: 0, return: "0"


### Complexity
- Time : O(n log n)
- Space : O(n)

---
