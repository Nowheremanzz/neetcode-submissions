"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_transfer = {None: None}
        curr = head
        while curr:
            node_transfer[curr] = Node(curr.val)
            curr = curr.next
        for old_n, new_n in node_transfer.items():
            if old_n:
                new_n.next = node_transfer[old_n.next]
                new_n.random = node_transfer[old_n.random]
        return node_transfer[head]