# N-Queens
- The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
- Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
- Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

---

## Approach
- Start from row 0.
- Try every column.
- If column or diagonal is occupied: Skip.
- Otherwise: Place queen.
- Mark:
  -  Column
  -  row-col
  -  row+col
- Recurse to next row.
- Undo all changes.


### Complexity
- Time : O(n!)
- Space : O(n)

---
