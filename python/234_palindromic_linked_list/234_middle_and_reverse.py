# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mid_ll(self, head):
        s = f = head
        while f and f.next and f.next.next: # have to return first half
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
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.mid_ll(head)
        second_half = mid.next
        reverse_second_half = self.reverse_ll(second_half)
        
        ans = True
        a = head
        b = reverse_second_half
        
        while a and b and ans:
            if a.val != b.val: ans = False
            a = a.next
            b = b.next
            
            
        return ans