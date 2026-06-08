# Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

---

## Approach
Key Insight
- The largest square will always come from one of the ends:
    - left end  -> largest negative number
    - right end -> largest positive number

Compare:
- abs(nums[left])
- abs(nums[right])
- The larger absolute value produces the larger square.

Two Pointers
- Left Pointer: Starts at left = 0
- Right Pointer: Starts at right = n - 1
- Position Pointer: Starts at pos = n - 1
- We fill the answer array from the end.

## Alogrithm
- Create an answer array of size n.
- Place one pointer at the beginning and one at the end.
- Compare absolute values of both ends.
- Square the larger value.
- Place it at the current position from the back.
- Move the corresponding pointer.
- Move the position pointer backward.
- Repeat until all positions are filled.

### Complexity 
- Time : O(n)
- Space : O(1)

---
