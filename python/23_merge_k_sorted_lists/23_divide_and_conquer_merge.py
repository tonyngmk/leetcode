# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_2_lists(self, l1, l2):
        s = head = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2            
        return s.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists: return None
        n = len(lists)
        interval = 1 # pointer helper to make pairs
        
        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = self.merge_2_lists(lists[i], lists[i+interval])
            interval *= 2
            
        return lists[0]
        