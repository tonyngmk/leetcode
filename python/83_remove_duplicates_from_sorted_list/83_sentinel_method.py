# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = ListNode(None)
        s.next = head
        i, j = s, s.next
        
        while j:
            if i.val == j.val: i.next = j.next
            else: i = i.next
            j = j.next
            
        return s.next
        