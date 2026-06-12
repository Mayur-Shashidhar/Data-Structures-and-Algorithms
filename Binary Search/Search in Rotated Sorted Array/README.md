# Search in Rotated Sorted Array
- There is an integer array nums sorted in ascending order (with distinct values).
- Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
- Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
- You must write an algorithm with O(log n) runtime complexity.

---

## Approach
- Use Binary Search as usual.
- Look at the middle element.
- First figure out which side is properly sorted:
    - Either the left side is sorted.
    - Or the right side is sorted.
    - One of them is always sorted.
- Once you know which side is sorted:
    - Check whether the target could possibly lie in that sorted range.
- If the target lies inside that sorted range:
    - Continue searching in that half.
- Otherwise:
    - Search in the other half.
- Repeat until:
    - You find the target, or
    - The search space becomes empty.
- If found: Return its index.
- If not found: Return -1.


### Complexity
- Time : O(log n)
- Space : O(1)

---
