# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        
        depth = 0
        q = collections.deque([root])
        
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                for c in [node.left, node.right]:
                    if c:
                        q.append(c)
                        
        return depth
        