# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque([root])
        ans = []
        
        while q:
            x = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                x += node.val
                
                for c in [node.left, node.right]:
                    if c:
                        q.append(c)
                        
            ans.append(float(x)/n)
            
        return ans
            