# Spiral Matrix (#54)
- Given an m x n matrix, return all elements of the matrix in spiral order.

---

## Example

Input:

```text id="0jsm8m"
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

Output:

```text id="x6yeyy"
[1,2,3,6,9,8,7,4,5]
```

Traversal:

```text id="z4ot19"
1 → 2 → 3
        ↓
4    5  6
↑       ↓
7 ← 8 ← 9
```

---

# Key Observation

The traversal always occurs along the boundary of the remaining matrix.

Maintain four boundaries:

```text id="8b43z5"
top
bottom
left
right
```

Initially:

```text id="jlwm101"
top = 0
bottom = rows - 1

left = 0
right = cols - 1
```

---

# Boundary Meaning

```text id="jlwm102"
top    -> first unvisited row

bottom -> last unvisited row

left   -> first unvisited column

right  -> last unvisited column
```

---

# Traversal Order

For every iteration:

### 1. Left → Right

Traverse:

```text id="jlwm103"
matrix[top][left...right]
```

Then:

```text id="jlwm104"
top += 1
```

because the top row has been visited.

---

### 2. Top → Bottom

Traverse:

```text id="jlwm105"
matrix[top...bottom][right]
```

Then:

```text id="jlwm106"
right -= 1
```

because the right column has been visited.

---

### 3. Right → Left

Traverse:

```text id="jlwm107"
matrix[bottom][right...left]
```

Then:

```text id="jlwm108"
bottom -= 1
```

because the bottom row has been visited.

---

### 4. Bottom → Top

Traverse:

```text id="jlwm109"
matrix[bottom...top][left]
```

Then:

```text id="jlwm110"
left += 1
```

because the left column has been visited.

---

# Algorithm

### Step 1

Initialize:

```text id="jlwm111"
top
bottom
left
right
```

---

### Step 2

Repeat while:

```text id="jlwm112"
top <= bottom
and
left <= right
```

---

### Step 3

Traverse:

```text id="jlwm113"
Left → Right
```

Update:

```text id="jlwm114"
top += 1
```

---

### Step 4

Traverse:

```text id="jlwm115"
Top → Bottom
```

Update:

```text id="jlwm116"
right -= 1
```

---

### Step 5

If:

```text id="jlwm117"
top <= bottom
```

Traverse:

```text id="jlwm118"
Right → Left
```

Update:

```text id="jlwm119"
bottom -= 1
```

---

### Step 6

If:

```text id="jlwm120"
left <= right
```

Traverse:

```text id="jlwm121"
Bottom → Top
```

Update:

```text id="jlwm122"
left += 1
```

---

### Step 7

Continue until all elements are visited.

---

# Dry Run

Input:

```text id="jlwm123"
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

Initial:

```text id="jlwm124"
top = 0
bottom = 2

left = 0
right = 2
```

---

## Left → Right

Visit:

```text id="jlwm125"
1 2 3
```

Answer:

```text id="jlwm126"
[1,2,3]
```

Update:

```text id="jlwm127"
top = 1
```

---

## Top → Bottom

Visit:

```text id="jlwm128"
6 9
```

Answer:

```text id="jlwm129"
[1,2,3,6,9]
```

Update:

```text id="jlwm130"
right = 1
```

---

## Right → Left

Visit:

```text id="jlwm131"
8 7
```

Answer:

```text id="jlwm132"
[1,2,3,6,9,8,7]
```

Update:

```text id="jlwm133"
bottom = 1
```

---

## Bottom → Top

Visit:

```text id="jlwm134"
4
```

Answer:

```text id="jlwm135"
[1,2,3,6,9,8,7,4]
```

Update:

```text id="jlwm136"
left = 1
```

---

## Final Iteration

Only one element remains:

```text id="jlwm137"
5
```

Final Answer:

```text id="jlwm138"
[1,2,3,6,9,8,7,4,5]
```

---

# Why Extra Conditions Are Needed

Before traversing:

```text id="jlwm139"
Right → Left
```

check:

```text id="jlwm140"
top <= bottom
```

Before traversing:

```text id="jlwm141"
Bottom → Top
```

check:

```text id="jlwm142"
left <= right
```

These prevent revisiting elements when the boundaries cross.

---

# Complexity
- Time : O(m * n)
- Space : O(1)`

---
