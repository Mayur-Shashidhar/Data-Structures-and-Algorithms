# Permutations II
- Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

---

## Approach
- Sort the array.
- Create visited array.
- Loop over all numbers.
- Skip visited numbers.
- Skip duplicate branches.
- Choose.
- Mark visited.
- Recurse.
- Undo.
- Unmark visited.


### Complexity
- Time : O(n × n!)
- Space : O(n)

---
