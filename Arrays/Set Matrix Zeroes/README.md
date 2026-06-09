# Set Matrix Zeroes
- Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
- You must do it in place.

---

## Approach 1: Brute Force
- Traverse the matrix.
    - Whenever: matrix[i][j] == 0
    - Store: (i, j)
- For every stored position: (row, col)
    - Make: 
        - Entire row = 0
        - Entire column = 0


### Complexity
- Time : O((m*n)*(m+n))
- Space : O(m*n)

---

## Approach 2: Row & Column Marking
- Create:
    - row[m]
    - col[n]
- Where: row[i] = 1
    - means: Row i should become zero
    - and col[j] = 1
    - means: Column j should become zero
- Traverse the matrix.
    - Whenever: matrix[i][j] == 0
    - mark:
        - row[i] = 1
        - col[j] = 1
- Traverse the matrix again.
- If: row[i] == 1 or col[j] == 1
    - then: matrix[i][j] = 0


## Complexity
- Time : O(m*n)
- Space : O(m+n)

---

# Approach 3: Optimal (First Row & First Column as Markers)

Instead of using:

```text
row[]
col[]
```

we can use:

```text
matrix[i][0]
matrix[0][j]
```

as marker arrays.

---

## Marker Meaning

### Row Marker

```text
matrix[i][0] = 0
```

means:

```text
Row i should become zero
```

---

### Column Marker

```text
matrix[0][j] = 0
```

means:

```text
Column j should become zero
```


## Algorithm

### Step 1: Mark Rows and Columns

Traverse the matrix.

Whenever:

```text
matrix[i][j] == 0
```

mark:

```text
matrix[i][0] = 0
matrix[0][j] = 0
```

If first column contains a zero:

```text
col0 = 0
```

---

### Step 2: Apply Markers

Traverse from:

```text
Bottom-right
```

towards:

```text
Top-left
```

If:

```text
matrix[i][0] == 0
```

or

```text
matrix[0][j] == 0
```

then:

```text
matrix[i][j] = 0
```

---

### Step 3: Handle First Column

If:

```text
col0 == 0
```

make the entire first column zero.

---

## Why Traverse from Bottom-Right?

Because:

```text
matrix[i][0]
matrix[0][j]
```

contain marker information.

If we overwrite them too early, we lose the information required for later cells.

Traversing from bottom-right preserves markers until they are fully used.


### Complexity
- Time : O(m*n)
- Space : O(1)

---
