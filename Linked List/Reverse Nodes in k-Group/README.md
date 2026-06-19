# Reverse Nodes in k-Group
- Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
- k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
- You may not alter the values in the list's nodes, only nodes themselves may be changed.

--- 

## Approach
- Create a dummy node before the head of the linked list.
- Use a pointer to identify the start of each group.
- Check whether there are at least k nodes available in the current group.
- If fewer than k nodes remain, stop and leave the remaining nodes unchanged.
- Reverse the current group of k nodes.
- Connect the reversed group back to the previous part of the linked list.
- Move to the next group.
- Repeat until the end of the linked list is reached.
- Return dummy.next.


### Complexity
- Time : O(n)
- Space : O(1)

---
