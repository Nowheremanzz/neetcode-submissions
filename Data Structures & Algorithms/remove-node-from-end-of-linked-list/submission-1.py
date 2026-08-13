# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head: Optional[ListNode], count: int, n: int) -> None:
            if not head:
                return None, count
            temp, count = remove(head.next, count, n)
            count += 1
            if count == n - 1:
                return head, count
            elif count == n:
                head.next = None
            elif count == n + 1:
                head.next = temp
            return temp, count
        temp, count = remove(head.next, 0, n)
        if count == n - 1:
            return head.next
        elif count == n:
            head.next = temp
        return head
            