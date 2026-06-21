# Daily Temperatures
- Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

---

## Approach
- Create an answer array filled with zeros.
- Create an empty stack that stores indices.
- Traverse the temperature array from left to right.
- While the stack is not empty and the current temperature is greater than the temperature at the index on top of the stack:
    - Pop the index.
    - Calculate the number of days waited.
    - Store it in the answer array.
- Push the current index onto the stack.
- Continue until all temperatures are processed.
- Any indices left in the stack have no warmer future day, so their answer remains 0.
- Return the answer array.


### Complexity
- Time : O(n)
- Space : O(n)

---
