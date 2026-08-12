# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        else:
            a = None
            b = None
            while head:
                b = head
                head = head.next
                b.next = a
                a = b
        return b
