# Find First and Last Position of Element in Sorted Array
- Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
- If target is not found in the array, return [-1, -1].
- You must write an algorithm with O(log n) runtime complexity.

---

## Approach
### First Search (Find First Position)
- Use Binary Search.
- If target is found:
    - Store its index as a possible answer.
    - Continue searching on the left side.
- Keep doing this until the search ends.
- The stored index will be the first occurrence.

### Second Search (Find Last Position)
- Use Binary Search again.
- If target is found:
    - Store its index as a possible answer.
    - Continue searching on the right side.
- Keep doing this until the search ends.
- The stored index will be the last occurrence.


### Complexity
- Time : O(log n)
- Space : O(1)

---
