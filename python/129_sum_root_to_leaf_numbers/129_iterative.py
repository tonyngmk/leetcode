# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, str(root.val))]
        
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right: ans += int(val)
            for c in [node.left, node.right]:
                if c:
                    stack.append((c, val+str(c.val)))
                    
        return ans
        
        