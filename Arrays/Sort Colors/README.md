# Sort Colors
- Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
- We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
- You must solve this problem without using the library's sort function.

---

## Approach 1: Counting Sort
- Traverse the array and count:
    - count_zero
    - count_one
    - count_two
- Fill the array with:
    - count_zero times -> 0
    - count_one times  -> 1
    - count_two times  -> 2


### Complexity
- Time : O(n)
- Space : O(1)

---

## Approach 2: Dutch National Flag Algorithm (Optimal)

## Key Observation

The array contains only three distinct values:

```text
0
1
2
```

Instead of counting and rewriting, we can partition the array into regions.

---

## Three Pointers

Maintain:

```text
low
mid
high
```

Initially:

```text
low = 0
mid = 0
high = n - 1
```

---

## Regions

At any point:

```text
0 ... low-1      -> all 0s

low ... mid-1    -> all 1s

mid ... high     -> unknown

high+1 ... end   -> all 2s
```

---

## Rules

### Case 1: nums[mid] == 0

0 belongs on the left side.

Swap:

```text
nums[low] ↔ nums[mid]
```

Move:

```text
low += 1
mid += 1
```

---

### Case 2: nums[mid] == 1

1 is already in the correct region.

Move:

```text
mid += 1
```

---

### Case 3: nums[mid] == 2

2 belongs on the right side.

Swap:

```text
nums[mid] ↔ nums[high]
```

Move:

```text
high -= 1
```

Important:

```text
Do NOT move mid
```

because the new element coming from the right side has not been processed yet.


### Complexity Analysis
- Time : O(n)
- Space : O(1)

---
