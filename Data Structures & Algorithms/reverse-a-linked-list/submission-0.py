# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        current = head
        
        while current:
            values.append(current.val)
            current = current.next

        tail = None
        n = len(values)
        for i in range(n):
            formar = ListNode(val = values[i], next = tail)
            tail = formar
            
        
        return tail