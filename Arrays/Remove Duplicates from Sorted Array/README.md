# Remove Duplicates from Sorted Array
- Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
- Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
- The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

---

## Approach: Two Pointers
- Assume the first element is unique.
- Initialize i = 0.
- Traverse the array using j from index 1.
- If nums[j] != nums[i]:
    - A new unique element is found.
    - Increment i.
    - Place nums[j] at position i.
5. Continue until the end of the array.
6. Return i + 1.

### Complexity
- Time : O(n)
- Space : O(1)

---
