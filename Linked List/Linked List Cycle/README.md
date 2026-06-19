# Linked List Cycle
- Given head, the head of a linked list, determine if the linked list has a cycle in it.
- There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
- Return true if there is a cycle in the linked list. Otherwise, return false.

---

## Approach
- Create two pointers:
    - slow
    - fast
- Both start at the head.
- Move:
    - slow one step at a time.
    - fast two steps at a time.
- If there is no cycle: fast will eventually reach None.
- If there is a cycle: fast will eventually catch up to slow.
- If the two pointers meet: Return True.
- If the loop ends: Return False.


### Complexity
- Time : O(n)
- Space : O(1)

---
