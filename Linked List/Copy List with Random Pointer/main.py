"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        copies = {}
        curr = head

        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next

        return copies[head]
