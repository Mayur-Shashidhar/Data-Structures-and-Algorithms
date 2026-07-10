# Find K Pairs with Smallest Sums
- You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
- Define a pair (u, v) which consists of one element from the first array and one element from the second array.
- Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

---

## Approach
- Create a Min Heap.
- Insert (nums1[i], nums2[0]) for first min(k, len(nums1)) elements.
- While heap not empty and answer size < k
    - Pop smallest pair.
    - Add it to answer.
    - Push next pair using same nums1 element and next nums2 element.
- Return answer.


### Complexity
- Time : O(k log k)
- Space : O(k)

---
