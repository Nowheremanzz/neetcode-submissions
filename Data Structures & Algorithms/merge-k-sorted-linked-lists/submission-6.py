# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwo(self, l: ListNode, r: ListNode):
        dummy_node = ListNode()
        curr = dummy_node
        while l and r:
            if l.val <= r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        if l:
            curr.next = l
        if r:
            curr.next = r
        return dummy_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        m = (len(lists) - 1) // 2
        l_half, r_half = lists[:m + 1], lists[m + 1:]
        l = self.mergeKLists(l_half)
        r = self.mergeKLists(r_half)
        return self.mergeTwo(l,r)
            