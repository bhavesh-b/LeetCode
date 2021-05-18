# Reversing a linked list using iterative method


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current!= None:
            nextp = current.next
            current.next = prev
            prev = current
            current = nextp
        return prev
        
        
