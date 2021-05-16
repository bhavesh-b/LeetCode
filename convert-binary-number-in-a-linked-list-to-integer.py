# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) :
        
        s = 0
        
        while head:
            s *= 2
            
            s += head.val
            
            head = head.next
        
        return s
