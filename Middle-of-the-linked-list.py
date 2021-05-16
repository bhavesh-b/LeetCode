# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

#Using the two pointer approach 
    
    def middleNode(self, head: ListNode) :
        fast = head 
        slow = head
        while (fast and fast.next) :   #when the slow pointer moves by one , the fast moves by two and when it reaches none , slow pointer is at the middle element
            slow = slow.next
            fast = fast.next.next
        
        return slow
            
    
