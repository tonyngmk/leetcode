# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                for c in [node.left, node.right]:
                    if c:
                        q.append(c)
                        
        return root
        