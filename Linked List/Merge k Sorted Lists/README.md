# Merge k Sorted Lists
- You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
- Merge all the linked-lists into one sorted linked-list and return it.

---

## Approach
- If the list of linked lists is empty, return None.
- Merge the linked lists in pairs.
- Take two lists at a time and merge them into one sorted list.
- Store the merged lists in a new array.
- Repeat the process until only one linked list remains.
- Return the final merged linked list.


### Complexity
- Time : O(N log k)
- Space : O(1)

---
