# Intersection of Two Arrays
- Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

---

## Approach
- Convert nums1 into a HashSet.
- Create another set to store the answer.
- Traverse nums2.
- For each element:
    - Check whether it exists in the HashSet.
    - If it exists, add it to the answer set.
- Convert the answer set into a list and return it.


### Complexity
- Time  : O(n + m)
- Space : O(n + k)

---
