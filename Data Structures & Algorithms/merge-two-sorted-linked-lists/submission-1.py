# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        accum = ListNode() if list1 or list2 else None
        res = accum
        
        while list1 or list2:
            if not list1:
                accum.val = list2.val
                list2 = list2.next
                accum.next = ListNode() if list2 else None
                accum = accum.next
            elif not list2:
                accum.val = list1.val
                list1 = list1.next
                accum.next = ListNode() if list1 else None
                accum = accum.next
            else:
                if list1.val > list2.val:
                    accum.val = list2.val
                    list2 = list2.next
                    accum.next = ListNode()
                    accum = accum.next
                else:
                    accum.val = list1.val
                    list1 = list1.next
                    accum.next = ListNode()
                    accum = accum.next

        return res

            