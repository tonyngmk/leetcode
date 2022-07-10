# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        
        odd = head
        # create another linked list
        even = head.next
        evenHead = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        # link 2 up
        odd.next = evenHead
        return head