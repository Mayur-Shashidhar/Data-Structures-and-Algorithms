# Next Greater Element II
- Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
- The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

---

## Approach
- Create an answer array initialized with -1.
- Create an empty stack to store indices.
- Traverse the array twice (2 * n iterations).
- Use modulo operation to get the actual index.
- While the stack is not empty and the current number is greater than the number at the index on top of the stack:
    - Pop the index.
    - Set its next greater element.
- During the first pass only:
    - Push indices into the stack.
- After traversal, any remaining indices have no next greater element.
- Return the answer array.


### Complexity
- Time : O(n)
- Space : O(n)

---
