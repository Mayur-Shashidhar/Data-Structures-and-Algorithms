# Merge Two Sorted Lists
- You are given the heads of two sorted linked lists list1 and list2.
- Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
- Return the head of the merged linked list.

---

## Approach
- Create a dummy node to act as the starting point of the merged list.
- Create a pointer called tail and point it to the dummy node.
- Compare the current nodes of both lists.
- If the value in the first list is smaller:
    - Attach that node to tail.
    - Move the first list pointer forward.
- Otherwise:
    - Attach the node from the second list to tail.
    - Move the second list pointer forward.
- Move tail forward.
- Repeat until one of the lists becomes empty.
- Attach the remaining nodes of the non-empty list to the merged list.
- Return dummy.next, since the dummy node itself is not part of the answer.


### Complexity
- Time : O(n + m)
- Space : O(1)

---
