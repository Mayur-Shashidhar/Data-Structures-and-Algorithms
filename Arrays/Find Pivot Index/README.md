# Find Pivot Index
- Given an array of integers nums, calculate the pivot index of this array.
- The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
- If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
- Return the leftmost pivot index. If no such index exists, return -1.

---

## Approach (Brute-Force)


For every index:

1. Calculate the sum of all elements to the left.
2. Calculate the sum of all elements to the right.
3. Compare both sums.
4. If they are equal, return the current index.


### Complexity Analysis
- Time : O(n²)
- Space Complexity : O(1)

---

## Approach (Prefix Sum)

Repeatedly calculating left and right sums is inefficient.

Instead:

1. Calculate the total sum once.
2. Maintain the left sum while traversing.
3. Derive the right sum using a formula.

---

## Key Formula

```text
total_sum = left_sum + nums[i] + right_sum
```

Therefore:

```text
right_sum = total_sum - left_sum - nums[i]
```

This allows us to compute the right sum in O(1).


### Complexity Analysis
- Time : O(n)
- Space : O(1)

---
