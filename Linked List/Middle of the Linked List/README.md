# Middle of the Linked List
- Given the head of a singly linked list, return the middle node of the linked list.
- If there are two middle nodes, return the second middle node.

---

## Approach
- Initialize:
    - slow = head
    - fast = head
- While:
    - fast exists
    - fast.next exists
- Move:
    - slow = slow.next
    - fast = fast.next.next
- When the loop ends: slow points to the middle node.
- Return slow.


### Complexity
- Time : O(n)
- Space : O(1)

---
