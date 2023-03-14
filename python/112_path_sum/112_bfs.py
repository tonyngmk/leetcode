# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: return root
        q = collections.deque([(root, targetSum-root.val)])
        
        while q:
            for _ in range(len(q)):
                node, val = q.popleft()
                if not val and not node.left and not node.right: return True
                for c in [node.left, node.right]:
                    if c:
                        q.append((c, val-c.val))
                        
        return False
                