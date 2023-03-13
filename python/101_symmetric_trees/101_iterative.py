# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = collections.deque([(root)])
        q.append(root)
        
        while q:
            l, r = q.popleft(), q.popleft()
            if not l and not r: continue
            if not l or not r: return False
            if l.val != r.val: return False

            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
                
        return True
        