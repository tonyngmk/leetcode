# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        s = ListNode(None)
        s.next = head
        i = s
        j = i.next
        
        while j:
            if j.val == val: i.next = j.next
            else: i = i.next
            j = j.next
        return s.next