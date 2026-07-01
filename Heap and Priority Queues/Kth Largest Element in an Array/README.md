# Kth Largest Element in an Array
- Given an integer array nums and an integer k, return the kth largest element in the array.
- Note that it is the kth largest element in the sorted order, not the kth distinct element.

---

## Approach
- Create an empty Min Heap.
- Push every number.
- If heap size > k: Pop the smallest.
- Return heap[0].


### Complexity
- Time  : O(n log k)
- Space : O(k)

---
