# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        next_head = self.reverseKGroup(curr, k)
        curr = head
        pre = next_head
        for _ in range(k):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre
            