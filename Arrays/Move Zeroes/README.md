# Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

---

## Two Pointer Approach

Use two pointers:

### Slow Pointer (`i`)

* Points to the position where the next non-zero element should be placed.

### Fast Pointer (`j`)

* Traverses the entire array.
* Finds non-zero elements.


## Algorithm
- Initialize i = 0.
- Traverse the array using j.
- If nums[j] is non-zero:
    - Swap `nums[i]` and `nums[j]`.
    - Increment `i`.
- Continue until the end of the array.

### Complexity
- Time : O(n)
- Space : O(1)

---
