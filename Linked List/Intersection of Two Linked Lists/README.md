# Intersection of Two Linked Lists
- Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

---

## Approach
- Create two pointers:
    - pA starting at headA.
    - pB starting at headB.
- Move both pointers one step at a time.
- When pA reaches the end of List A: Move it to headB.
- When pB reaches the end of List B: Move it to headA.
- Continue moving both pointers.
- If the lists intersect: The pointers will eventually meet at the intersection node.
- If the lists do not intersect: Both pointers will eventually become None.
- Return the node where they meet.


### Complexity
- Time : O(n + m)
- Space : O(1)

---
