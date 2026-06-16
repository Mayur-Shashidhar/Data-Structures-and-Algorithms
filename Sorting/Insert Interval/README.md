# Insert Interval
- You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
- Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
- Return intervals after the insertion.
- Note that you don't need to modify intervals in-place. You can make a new array and return it.

---

## Approach
- Create an empty answer list.
- Traverse all intervals.
- If the current interval is completely before the new interval:
    - Add it directly to the answer.
- If the current interval is completely after the new interval:
    - Add the new interval to the answer.
    - From now on, treat the current interval as the new interval.
    - This ensures the new interval is inserted only once.
- If the current interval overlaps with the new interval:
    - Merge them.
    - Update the start and end of the new interval.
- Continue until all intervals are processed.
- Add the final merged new interval to the answer.
- Return the answer.


### Complexity
- Time : O(n)
- Space : O(n)

---
