# Search Insert Position
- Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
- You must write an algorithm with O(log n) runtime complexity.

---

## Approach
- Since the array is sorted, use Binary Search.
- Look at the middle element.
- If the middle element is the target:
    - Return its index.
- If the target is bigger than the middle element:
    - Ignore the left half.
    - Search in the right half.
- If the target is smaller than the middle element:
    - Ignore the right half.
    - Search in the left half.
- Keep doing this until:
    - You find the target, OR
    - There is no search space left.
- If the target is not found:
    - Return the position where it should be inserted.
    - After Binary Search ends, the left pointer automatically points to that position.


### Complexity
- Time : O(log n)
- Space : O(1)

---
