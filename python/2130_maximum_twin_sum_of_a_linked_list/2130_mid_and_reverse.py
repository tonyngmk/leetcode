# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middle_ll(self, head):
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s

    def reverse_ll(self, head):
        i, j = None, head
        while j:
            k = j.next
            j.next = i
            i = j
            j = k
        return i

    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        mid = self.middle_ll(head)
        reverse = self.reverse_ll(mid)

        while reverse:
            ans = max(ans, head.val + reverse.val)
            head = head.next
            reverse = reverse.next

        return ans
