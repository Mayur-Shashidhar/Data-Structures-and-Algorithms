# Concatenation of Array
- Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
- Specifically, ans is the concatenation of two nums arrays.
- Return the array ans.

---

## Approach
- Find the length of array nums as n.
- Initialize array ans with size 2n.
- Array ans is nums + nums.
- Return ans


### Complexity
- Time : O(1)
- Space : O(n)

---
