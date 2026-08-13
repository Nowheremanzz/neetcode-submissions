# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode()
        curr = dummy_node
        heap = []
        for ind, n in enumerate(lists):
            if n:
                heapq.heappush(heap, [n.val, ind])
        while heap:
            minimum, ind = heapq.heappop(heap)
            curr.next = lists[ind]
            lists[ind] = lists[ind].next
            curr = curr.next
            if lists[ind]:
                heapq.heappush(heap, [lists[ind].val, ind])
        return dummy_node.next