# Palindrome Linked List
- Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

---

## Approach
- Find the middle of the linked list using Fast and Slow Pointers.
- Reverse the second half of the linked list.
- Compare the first half and the reversed second half node by node.
- If any values differ, return False.
- If all values match, return True.


### Complexity
- Time : O(n)
- Space : O(1)

---
