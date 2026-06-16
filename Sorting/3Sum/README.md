# 3Sum
- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
- Notice that the solution set must not contain duplicate triplets.

--- 

## Approach
- Sort the array.
- Fix one element at a time.
- Use two pointers on the remaining array.
- Calculate the sum of:
    - fixed number
    - left pointer
    - right pointer
- If sum is:
    - Zero → store triplet
    - Too small → move left
    - Too large → move right
- Skip duplicate values to avoid duplicate triplets.
- Continue until all positions are processed.


### Complexity
- Time : O(n²)
- Space : O(1)

---
