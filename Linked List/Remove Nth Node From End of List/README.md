# Remove Nth Node From End of List
- Given the head of a linked list, remove the nth node from the end of the list and return its head.

---

## Approach
- Create a dummy node and connect it before the head.
- Place both slow and fast at the dummy node.
- Move the fast pointer n steps ahead.
- Now move both pointers one step at a time.
- Continue until fast.next becomes None.
- At this point: slow will be just before the node that needs to be removed.
- Remove the node by changing pointers: slow.next = slow.next.next
- Return: dummy.next


### Complexity
- Time : O(n)
- Space : O(1)

---
