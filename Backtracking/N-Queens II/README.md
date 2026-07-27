# N-Queens II
- The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
- Given an integer n, return the number of distinct solutions to the n-queens puzzle.

---

## Approach
- Start from row 0.
- Try every column.
- Skip unsafe positions.
- Place queen.
- Mark:
  -  Column
  -  row-col
  -  row+col
- Recurse to next row.
- Undo.
- Every time row == n: Increase count.


### Complexity
- Time : O(n!)
- Space : O(n)

---
