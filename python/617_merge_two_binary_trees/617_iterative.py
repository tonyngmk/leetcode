# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1: return root2
        if not root2: return root1
        
        q = collections.deque([(root1, root2)])
        
        while q:
            for _ in range(len(q)):
                a, b = q.popleft()
                if not b: continue
                a.val += b.val
                
                if not a.left: a.left = b.left
                else: q.append((a.left, b.left))
                    
                if not a.right: a.right = b.right
                else: q.append((a.right, b.right))

        return root1            
        