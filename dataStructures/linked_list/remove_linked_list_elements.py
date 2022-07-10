# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        i, j = sentinel, head
        
        while j:
            if j.val == val:
                i.next = j.next
            else:
                i = j
            j = j.next
            
        return sentinel.next