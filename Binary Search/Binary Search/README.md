## Binary Search
- Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
- - You must write an algorithm with O(log n) runtime complexity.

---

## Approach
1. Maintain left and right pointers.
2. Find middle element.
3. Compare nums[mid] with target.
4. If equal → return index.
5. If target is larger → search right half.
6. If target is smaller → search left half.
7. Repeat until left > right.
8. If not found → return -1.

### Complexity
- Time : O(log n)
- Space : O(1)

---
