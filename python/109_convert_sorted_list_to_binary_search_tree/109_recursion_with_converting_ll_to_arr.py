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
    def ll_to_arr(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = self.ll_to_arr(head)
        
        def list_to_bst(l, r):
            if l > r: return None
            
            mid = l + (r-l)//2
            node = TreeNode(arr[mid])
            
            # Base case, 1 node left
            if l == r: return node
            
            # Recursive case
            node.left = list_to_bst(l, mid-1)
            node.right = list_to_bst(mid+1, r)
            return node
        
        return list_to_bst(0, len(arr)-1)
        