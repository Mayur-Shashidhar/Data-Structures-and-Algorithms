# Single Number
- Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
- You must implement a solution with a linear runtime complexity and use only constant extra space.

---

## Approach
- Initialize result = 0
- XOR every element with result
- Duplicate elements cancel each other.
    - a ^ a = 0
    - a ^ 0 = a
- The unique element remains.

### Complexity 
- Time : O(n)
- Space : O(1)

---
