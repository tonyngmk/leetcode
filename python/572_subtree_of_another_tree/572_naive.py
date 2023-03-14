# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, a, b):
        q = collections.deque([(a, b)])
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if not x and not y: continue
                if not x or not y: return False
                if x.val != y.val: return False
                q.append((x.left, y.left))
                q.append((x.right, y.right))
                
        return True
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        q = collections.deque([root])
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.val == subRoot.val and self.check(node, subRoot): return True
                for c in [node.left, node.right]:
                    if c:
                        q.append(c)
                        
        return False
                    
                
        