# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        i, j = None, head
        
        while j:
            k = j.next
            j.next = i
            i = j
            j = k
            
        return i