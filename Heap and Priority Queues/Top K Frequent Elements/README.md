# Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

---

## Approach
- Count frequencies.
- Create Min Heap.
- Push (frequency, number).
- If heap size > k: Pop smallest frequency.
- Return numbers from heap.


### Complexity
- Time : O(n log k)
- Space : O(n)

---
