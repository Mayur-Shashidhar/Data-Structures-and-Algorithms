# Multiply Strings
- Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
- Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

---

## Approach
- If either number is "0", return "0" immediately.
- Create a result array of size len(num1) + len(num2) initialized to zeros.
- Reverse both input strings so index 0 corresponds to the ones place.
- For each pair of indices (i1, i2):
    - Multiply the corresponding digits.
    - Add the product to res[i1 + i2].
    - Propagate any carry to res[i1 + i2 + 1].
    - Keep only the ones digit at res[i1 + i2].
- Reverse the res array, skip leading zeros, and join the digits into a string.


### Complexity
- Time : O(m * n)
- Space : O(m + n)

---
