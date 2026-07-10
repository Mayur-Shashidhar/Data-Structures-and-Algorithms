# Find K Closest Elements
- Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
- An integer a is closer to x than an integer b if:
    - |a - x| < |b - x|, or
    - |a - x| == |b - x| and a < b

---

## Approach
- Create a Max Heap.
- For every number:
    - Compute distance = abs(num - x)
    - Push (-distance, -num)
- If heap size exceeds k then Pop farthest element.
- Extract remaining numbers.
- Sort answer.


### Complexity
- Time : O(n log k)
- Space : O(k)

---
