# Merge Intervals
- Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

---

## Approach
- Sort the intervals based on their start time.
- Add the first interval to the answer.
- Traverse the remaining intervals one by one.
- For each interval, compare it with the last interval in the answer.
- If the current interval overlaps with the last interval:
    - Merge them.
    - Update the ending value of the last interval.
- If the current interval does not overlap:
    - Add it as a new interval to the answer.
- Continue until all intervals are processed.
- Return the answer.


### Complexity
- Time : O(n log n)
- Space : O(n)

---
