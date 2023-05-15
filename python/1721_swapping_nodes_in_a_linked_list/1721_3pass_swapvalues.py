# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1

        front = head
        for i in range(1, k):
            front = front.next

        end = head
        for i in range(length-k):
            end = end.next

        front.val, end.val = end.val, front.val
        return head