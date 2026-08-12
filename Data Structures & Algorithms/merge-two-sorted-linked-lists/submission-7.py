# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        dummy_node = ListNode()
        curr = dummy_node
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                if not list1.next:
                    list1.next = list2
                    break
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                if not list2.next:
                    list2.next = list1
                    break
                list2 = list2.next
        return dummy_node.next


