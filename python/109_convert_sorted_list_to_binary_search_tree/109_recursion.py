# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mid_ll(self, head):
        prev = None
        s = f = head
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next
            
        if prev: prev.next = None # after exiting loop, we disconnect previous
        return s
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return head
        
        mid = self.mid_ll(head)
        node = TreeNode(mid.val) # Create new starting node
        if head == mid: return node # Only 1 node, base case
        
        # Recursive case
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
        