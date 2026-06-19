# Linked List Cycle II
- Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
- There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
- Do not modify the linked list.

---

## Approach
- Initialize two pointers, slow and fast, at the head.
- Move slow one step and fast two steps until they meet or the list ends.
- If the list ends, return None because no cycle exists.
- If they meet, place a new pointer at the head of the list.
- Keep the other pointer at the meeting point.
- Move both pointers one step at a time.
- The node where they meet is the starting node of the cycle.
- Return that node.


### Complexity
- Time : O(n)
- Space : O(1)

---
