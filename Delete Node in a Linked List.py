# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #As mentioned it will not be the tail node    
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
  # Above code deletes a node in a singly-linked list
