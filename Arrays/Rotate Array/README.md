# Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

---

## Brute Force
- Create a new array of size of original array of nums: temp = [0] * n
- For every index i: temp[(i+k)%n] = nums[i]
- After filling temp, copy back to nums.

### Complexity
- Time : O(n)
- Space : O(n)

---

## Optimal Approach
- Reverse the entire array.
- Reverse first k elements.
- Reverse remaining elements.

### Complexity
- Time : O(n)
- Space : O(1)

---
