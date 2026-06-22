# 132 Pattern
- Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
- Return true if there is a 132 pattern in nums, otherwise, return false.

---

## Approach
- Create an empty stack.
- Maintain a variable second representing the best candidate for the "2" in the 132 pattern.
- Traverse the array from right to left.
- If the current number is smaller than second:
    - A valid 132 pattern exists.
    - Return True.
- While the stack is not empty and the current number is greater than the top of the stack:
    - Pop the stack.
    - Update second with the popped value.
- Push the current number into the stack.
- Continue until all elements are processed.
- If no pattern is found, return False.


### Complexity
- Time : O(n)
- Space : O(n)

---
