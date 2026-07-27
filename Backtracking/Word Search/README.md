# Word Search
- The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

---

## Approach
- Start DFS from every cell.
- If current character doesn't match: Return False.
- Mark the cell as visited.
- Explore:
    - Up
    - Down
    - Left
    - Right
- Restore the cell.
- If any direction succeeds: Return True.


### Complexity
- Time : O(m × n × 4^L)
- Space : O(L)

---
