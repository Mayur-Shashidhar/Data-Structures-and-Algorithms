# Running Sum of 1d Array
- Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
- Return the running sum of nums.

---

## Approach: In-Place Prefix Sum
- Start from index 1.
- Add the previous element to the current element.
- Store the result back in the current position.
- Continue until the end of the array.
- Return the modified array.

### Complexity
- Time : O(n)
- Space : O(1)

---
