# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
#         # Approach 1: Hash Set
#         seen = set()
#         while headB:
#             if headB not in seen: seen.add(headB)
#             headB = headB.next
        
#         while headA:
#             if headA in seen:
#                 return headA
#             headA = headA.next
            
#         return None
    
        # Approach 2: 2 pointer approach
        i = headA
        j = headB
        
        while i != j:
            i = headB if i is None else i.next
            j = headA if j is None else j.next
        
        return i