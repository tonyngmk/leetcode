# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        stack = [(root, 1)]
        ans = float('inf')
        
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right: ans = min(ans, depth)
            for c in [node.left, node.right]:
                if c:
                    stack.append((c, depth+1))
                    
        return ans