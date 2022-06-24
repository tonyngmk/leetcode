# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # Approach 1: Hash table
        # seen = set()
        # while head is not None:
        #     if head in seen:
        #         return head
        #     else:
        #         seen.add(head)
        #         head = head.next
        # return None
        
        # Approaoch 2: Floyd's Tortoise and Hare
        if head is None: return None # Not a LL?
        
        i = self.getIntersect(head)
        if i is None: # Not a cycle
            return None
        
        p1 = head
        p2 = i
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1 # will definitely intersect
        
        
    def getIntersect(self, head):
        s = head
        f = head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s: return s # return either s or f        
        return None
        
        