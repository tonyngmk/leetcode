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
        # Add sentinel node
        sentinel = ListNode(0)
        sentinel.next = head
        
        # Create pointers
        prev, curr = sentinel, head
        while curr:
            if curr.val==val: # Node at curr pointer to remove
                prev.next = curr.next # Join previous next pointer to curr's next pointer
            else:
                prev = curr # Not a removal situation, move up prev's poitner
            curr = curr.next # Always move up curr pointer
            
        return sentinel.next # Header