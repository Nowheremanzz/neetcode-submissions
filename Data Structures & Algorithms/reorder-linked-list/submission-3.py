# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None
        prev = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        sec = prev
        fir = head
        while sec:
            fir_next = fir.next
            sec_next = sec.next
            fir.next = sec
            sec.next = fir_next
            fir = fir_next
            sec = sec_next