# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def dfs(node, goLeft, steps):
            if node:
                self.length = max(self.length, steps)
                if goLeft:
                    dfs(node.left, True, 1)
                    dfs(node.right, False, steps+1)
                else:
                    dfs(node.left, True, steps+1)
                    dfs(node.right, False, 1)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.length