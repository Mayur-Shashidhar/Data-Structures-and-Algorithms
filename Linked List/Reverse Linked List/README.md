# Reverse Linked List
- Given the head of a singly linked list, reverse the list, and return the reversed list.

---

## Approach
- Create a pointer called prev and set it to None.
- Create another pointer called curr and set it to the head of the list.
- While curr is not None:
    - Store the next node in a temporary variable so we don't lose the rest of the list.
    - Reverse the current node's pointer by making it point to prev.
    - Move prev one step forward.
    - Move curr one step forward.
- Continue until all nodes have been processed.
- At the end, prev will be pointing to the new head of the reversed list.
- Return prev.


### Complexity
- Time : O(n)
- Space : O(1)

---
