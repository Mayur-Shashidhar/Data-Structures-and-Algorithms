# Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

---

## Approach
- Create an empty hashmap.
- Traverse the array.
- For each element:
    - Calculate complement = target - current element
    - Check of complement exist in hashmap
        - if yes -> answer found
        - if no -> store current element and its index
- Continue until answer is found.

### Complexity
- Time : O(n)
- Space : O(n)

---
