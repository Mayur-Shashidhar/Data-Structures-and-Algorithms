# Subarray Sum Equals K
- Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
- A subarray is a contiguous non-empty sequence of elements within an array.

---

## Approach
- Create a HashMap to store: prefix_sum → frequency
- Initialize:
    - prefix_sum = 0
    - count = 0
    - Put: 0 → 1 in the HashMap.
- Traverse the array.
- Add the current number to the running prefix sum.
- Check whether: prefix_sum - k already exists in the HashMap.
- If it exists:
    - Add its frequency to the answer.
    - Each occurrence represents a valid subarray.
- Store the current prefix sum in the HashMap.
- Continue until the array ends.
- Return the total count.


### Complexity
- Time : O(n)
- Space : O(n)

---
