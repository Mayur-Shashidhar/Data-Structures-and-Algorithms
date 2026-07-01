# K Closest Points to Origin
- Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
- The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
- You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

---

## Approach
- Create a Max Heap.
- For every point:
    - Compute distance.
    - Push into heap.
    - If heap size > k: Remove farthest.
- Return remaining points.


### Complexity
- Time : O(n log k)
- Space : O(k)

---
