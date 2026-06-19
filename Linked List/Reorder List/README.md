# Reorder List
- You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
- Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
- You may not modify the values in the list's nodes. Only nodes themselves may be changed.

---

## Approach
- Find the middle of the linked list using Fast and Slow Pointers.
- Split the linked list into two halves.
- Reverse the second half of the linked list.
- Take one node from the first half and one node from the reversed second half alternately.
- Continue merging until all nodes are reordered.
- Modify the list in-place.


### Complexity
- Time : O(n)
- Space : O(1)

---
