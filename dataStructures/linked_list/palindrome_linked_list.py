# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # obtain mid-way point via slow pointer
        
        # Reverse LL (from mid-way point)
        i = None
        while slow:
            k = slow.next
            slow.next = i
            i = slow
            slow = k
            
        while i:
            if i.val != head.val:
                return False
            i = i.next
            head = head.next
        return True