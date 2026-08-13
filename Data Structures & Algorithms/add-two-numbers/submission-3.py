# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            addition = a + b + carry
            new_val = addition % 10
            curr.next = ListNode(new_val)
            carry = addition // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
