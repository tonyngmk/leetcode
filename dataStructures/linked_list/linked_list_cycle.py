# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # # Approach 1: Hash table
        # ### Time: O(n)
        # ### Space: O(n)
        # seen = set()
        # while head is not None:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False
    
        # Approach 2: Floyd's Tortoise and Hare
        ### Time: O(n+m), where n is total nodes, and m is node in cycle
        ### Space: O(1), no extra space needed
        
        if head is None: return False # Empty
        s = head
        f = head.next # 1 step in front
        while s != f:
            if f is None or f.next is None:
                return False
            s = s.next
            f = f.next.next
        return True # If slow and fast are together 
            