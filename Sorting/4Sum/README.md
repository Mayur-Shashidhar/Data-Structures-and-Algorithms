# 4Sum
- Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target
- You may return the answer in any order.

---

## Approach
- Sort the array.
- Fix the first number.
- Fix the second number.
- Use two pointers on the remaining part of the array:
    - One pointer starts from the left.
    - One pointer starts from the right.
- Calculate: first + second + left + right
- If the sum equals the target:
    - Store the quadruplet.
    - Move both pointers.
    - Skip duplicates.
- If the sum is smaller than the target:
    - Move the left pointer right to increase the sum.
- If the sum is larger than the target:
    - Move the right pointer left to decrease the sum.
- Continue until the two pointers meet.
- Repeat for all choices of the first and second numbers.


### Complexity
- Time : O(n³)
- Space : O(1)

---
