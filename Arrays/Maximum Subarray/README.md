# Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

---

## Kadane's Algorithm
Maintain two variables:
- current_sum: Represents the maximum subarray sum ending at the current position.
- max_sum: Represents the maximum subarray sum found so far.

## Algorithm
- Initialize:
    - current_sum = nums[0]
    - max_sum = nums[0]
- Traverse the array from index 1.
- For every element:
    - Decide whether to:
        - Start a new subarray.
        - Extend the existing subarray.

    - Update:
        - current_sum = max(nums[i], current_sum + nums[i])

- Update:
    - max_sum = max(max_sum, current_sum)
- Return max_sum.

### Cmplexity
- Time : O(n)
- Space : O(1)

---
