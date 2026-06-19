# Add Two Numbers
- You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
- You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

## Approach
- Create a dummy node to build the answer linked list.
- Create a pointer called tail pointing to the dummy node.
- Maintain a variable called carry initialized to 0.
- Traverse both linked lists while at least one list still has nodes or there is a carry.
- Take the current value from each list. If a list has ended, use 0.
- Compute: sum = value1 + value2 + carry
- Create a new node with: sum % 10 and attach it to the answer list.
- Update carry: carry = sum // 10
- Move the pointers of both lists forward.
- Move the tail pointer forward.
- Return dummy.next.


### Complexity
- Time : O(max(n, m))
- Space : O(max(n, m))

---
