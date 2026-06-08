# Valid Palindrome
- A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
- Given a string s, return true if it is a palindrome, or false otherwise.

---

## Approach: Two Pointers

Use two pointers:
- Left Pointer (`left`): Starts from the beginning of the string.
- Right Pointer (`right`): Starts from the end of the string.



1. Initialize:

   * `left = 0`
   * `right = len(s) - 1`

2. While `left < right`:

   * Skip characters that are not alphanumeric.
   * Convert characters to lowercase.
   * Compare characters at both pointers.

3. If characters are different:

   * Return `False`.

4. If characters are equal:

   * Move both pointers inward.

5. If the loop completes:

   * Return `True`.


### Complexity Analysis
- Time : O(n)
- Space : O(1)

---
