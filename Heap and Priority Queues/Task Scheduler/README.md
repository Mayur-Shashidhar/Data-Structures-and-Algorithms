# Task Scheduler
- You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
- Return the minimum number of CPU intervals required to complete all tasks.

---

## Approach
- Count frequencies.
- Build a max heap.
- Maintain:
    - Current time
    - Cooldown queue
- Every unit of time:
    - Execute highest-frequency task.
    - Decrease its count.
    - Put it into cooldown if more executions remain.
    - If a task's cooldown finishes, push it back into the heap.
- Continue until both heap and queue are empty.


### Complexity
- Time : O(n)
- Space : O(26)

---
