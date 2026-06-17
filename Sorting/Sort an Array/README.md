# Sort an Array
- Given an array of integers nums, sort the array in ascending order and return it.
- You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

---

## Approach
- Find the middle of the array.
- Split the array into:
    - Left half
    - Right half
- Recursively sort both halves.
- Merge the two sorted halves into one sorted array.
- Continue until the entire array becomes sorted.

### Complexity
- Time : O(n log n)
- Space : O(n)

---
