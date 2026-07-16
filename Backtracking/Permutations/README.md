# Permutations
- Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

---

## Approach
- Create visited array.
- Loop through every number.
- Skip if already visited.
- Choose current number.
- Mark visited.
- Recurse.
- Undo.
- Unmark visited.


### Complexity
- Time : O(n × n!)
- Space : O(n)

---
