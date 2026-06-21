# Decode String
- Given an encoded string, return its decoded string.
- The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
- You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
- The test cases are generated so that the length of the output will never exceed 105.

---

## Approach
- Create an empty stack.
- Traverse the string character by character.
- If the character is a digit:
    - Build the complete number.
- If the character is '[':
    - Push the current string and current number onto the stack.
    - Reset both for processing the inner substring.
- If the character is a letter:
    - Append it to the current string.
- If the character is ']':
    - Pop the previous string and repeat count from the stack.
    - Repeat the current decoded string that many times.
    - Append it to the previous string.
- Continue until the entire string is processed.
- Return the final decoded string.


### Complexity
- Time : O(n)
- Space : O(n)

---
