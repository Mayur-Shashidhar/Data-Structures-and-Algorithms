# Find the Duplicate Number
- Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
- There is only one repeated number in nums, return this repeated number.
- You must solve the problem without modifying the array nums and using only constant extra space.

---

## Approach
- Treat each value in the array as a pointer to another index.
- This creates a virtual linked list.
- Use Fast and Slow Pointers to find a meeting point inside the cycle.
- Initialize:
    - slow = nums[0]
    - fast = nums[0]
- Move:
    - slow one step at a time.
    - fast two steps at a time.
- Continue until both pointers meet.
- Place a new pointer at the beginning of the array.
- Keep the other pointer at the meeting point.
- Move both pointers one step at a time.
- The position where they meet is the duplicate number.
- Return that number.


### Complexity
- Time : O(n)
- Space : O(1)

---
