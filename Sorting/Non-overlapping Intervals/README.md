# Non-overlapping Intervals
- Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
- Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

---

## Approach
- Sort intervals by their ending value.
- Keep the first interval.
- Traverse the remaining intervals.
- For each interval:
    - If it does not overlap with the previously kept interval:
        - Keep it.
    - If it overlaps:
        - Remove it.
        - Increase removal count.
- Return the number of removals.


### Complexity
- Time : O(n log n)
- Space : O(1)

---
