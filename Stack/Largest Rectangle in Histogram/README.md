# Largest Rectangle in Histogram
- Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

---

## Approach
- Create an empty stack.
- Store: (start_index, height)
- Traverse all bars.
- If the current height is greater than or equal to the stack top: Push it.
- If the current height is smaller: Pop bars until the stack becomes valid.
- For every popped bar:
    - Calculate width.
    - Calculate area.
    - Update maximum area.
- After processing all bars: Process remaining bars in the stack.
- Return the maximum area.


### Complexity
- Time : O(n)
- Space : O(n)

---
