# Longest Consecutive Sequence
- Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
- You must write an algorithm that runs in O(n) time.

---

# Brute Force Approach
For every number:

1. Check if the next number exists.
2. Then check the next one.
3. Continue until the sequence breaks.
4. Keep track of the longest sequence length.


### Complexity
- Time : O(n²)
- Space : O(1)

---

## Optimal Approach (HashSet)
We frequently need to answer:

```text
Does this number exist?
```

A HashSet provides:

```text
O(1)
```

average lookup time.

---

## Important Optimization

Consider the sequence:

```text
1,2,3,4
```

If we start counting from:

```text
1
```

we get the entire sequence.

Starting from:

```text
2
```

or

```text
3
```

would repeat work.

Therefore, only start counting from numbers that are the beginning of a sequence.

---

## Sequence Start Detection

A number is a sequence start if:

```text
num - 1 not in num_set
```

Example:

```text
1 -> Start
2 -> Skip
3 -> Skip
4 -> Skip
```

because:

```text
0 not present
1 present
2 present
3 present
```

---

## Algorithm

### Step 1

Insert all elements into a HashSet.

### Step 2

Traverse every number in the set.

### Step 3

Check:

```text
num - 1 not in num_set
```

If true:

```text
num is the start of a sequence
```

### Step 4

Count consecutive numbers:

```text
num + 1
num + 2
num + 3
...
```

until the sequence breaks.

### Step 5

Update the longest sequence length.

---

## Dry Run

Input:

```text
nums = [100,4,200,1,3,2]
```

HashSet:

```text
{100,4,200,1,3,2}
```

---

### num = 100

Check:

```text
99 not present
```

Start sequence.

Length:

```text
1
```

---

### num = 200

Check:

```text
199 not present
```

Start sequence.

Length:

```text
1
```

---

### num = 1

Check:

```text
0 not present
```

Start sequence.

Check:

```text
2 present
3 present
4 present
```

Length:

```text
4
```

Update longest.

---

### num = 2

Check:

```text
1 present
```

Not a sequence start.

Skip.

---

### num = 3

Check:

```text
2 present
```

Skip.

---

### num = 4

Check:

```text
3 present
```

Skip.

---

Final Answer:

```text
4
```


### Complexity
- Time : O(n)
- Space : O(n)

---
