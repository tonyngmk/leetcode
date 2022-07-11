# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head: return None
        if not head.next: return head
        
        n = 1
        i = head
        while i.next:
            i = i.next
            n+=1
        i.next = head
        
        k = k%n 
        indexToRemove = n-k-1
        
        a = head 
        for i in range(indexToRemove):
            a = a.next
        b = a.next
        a.next = None 
        
        return b
        