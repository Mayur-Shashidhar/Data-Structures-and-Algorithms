# Rearrange Array Elements by Sign
- You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
- You should return the array of nums such that the array follows the given conditions:
    1. Every consecutive pair of integers have opposite signs.
    2. For all integers with the same sign, the order in which they were present in nums is preserved.
    3. The rearranged array begins with a positive integer.
- Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

---

## Approach: Direct Placement
- Create a result array of size n.
- Maintain two indices:
    - pos = 0
    - neg = 1
    
    Where:
    - pos -> next even index
    - neg -> next odd index
- Traverse the input array.
- If current element is positive
    - Place it at: answer[pos]
    - Move: pos += 2
- If current element is negative
    - Place it at: answer[neg]
    - Move: neg += 2
- Return the answer array.


### Complexity
- Time : O(n)
- Space : O(n)

---
