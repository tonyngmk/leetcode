# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = collections.deque([(p, q)])
        
        while queue:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                if not a and not b: continue
                if not a or not b: return False
                if a.val != b.val: return False
                
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
                
        return True