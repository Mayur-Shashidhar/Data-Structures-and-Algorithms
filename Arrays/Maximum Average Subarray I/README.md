# Maximum Average Subarray I
- You are given an integer array nums consisting of n elements, and an integer k.
- Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

---

## Approach (Brute-Force)
Generate every possible subarray of size `k`.

For each subarray:

1. Calculate its sum.
2. Calculate its average.
3. Keep track of the maximum average.


## Algorithm

For every starting index:

1. Take the next `k` elements.
2. Compute their sum.
3. Compute the average.
4. Update the maximum average if needed.


### Complexity Analysis
- Time : O(n × k)
- Space : O(1)

---

## Approach (Sliding Window)

## Observation

Consecutive windows overlap heavily.

Example:

```text
[1,12,-5,-6]
```

Next Window:

```text
[12,-5,-6,50]
```

Notice:

```text
12, -5, -6
```

are already part of the previous window.

Recalculating the entire sum is unnecessary.


## Key Idea

When moving the window:

```text
Remove the outgoing element.
Add the incoming element.
```

Instead of recomputing the entire sum:

```text
new_window_sum
=
old_window_sum
- outgoing_element
+ incoming_element
```


## Algorithm

### Step 1

Calculate the sum of the first window of size `k`.

Example:

```text
[1,12,-5,-6]
```

Sum:

```text
2
```

Initialize:

```text
window_sum = 2
max_sum = 2
```

---

### Step 2

Slide the window one position to the right.

Current:

```text
[1,12,-5,-6]
```

Next:

```text
[12,-5,-6,50]
```

Update:

```text
window_sum
=
2 - 1 + 50
=
51
```

Update:

```text
max_sum = 51
```

---

### Step 3

Slide again.

Current:

```text
[12,-5,-6,50]
```

Next:

```text
[-5,-6,50,3]
```

Update:

```text
window_sum
=
51 - 12 + 3
=
42
```

No update to maximum.

---

### Final Result

Maximum Window Sum:

```text
51
```

Average:

```text
51 / 4
=
12.75
```

### Complexity
- Time : O(n)
- Space Complexity : O(1)

---
