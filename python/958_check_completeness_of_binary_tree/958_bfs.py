# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        null_found = False
        q = collections.deque([root])
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if not node: null_found = True
                else:
                    if null_found: return False
                    for c in [node.left, node.right]:
                        q.append(c)
        return True