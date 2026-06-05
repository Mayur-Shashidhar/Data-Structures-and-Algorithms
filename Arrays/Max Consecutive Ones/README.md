# Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

---

## Approach
- Take two variables:
current: current consecutive 1's count
maximum: largest streak found so far
- Go through each element:

If element is 1:
- a. Increase current by 1
- b. Update maximum if current becomes larger

If element is 0:
- a. The streak breaks
- b. Reset current to 0

### Complexity
- Time : O(n)
- Space : O(1)

---
