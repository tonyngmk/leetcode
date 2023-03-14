# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = curr = 0
        
        while root:
            # if left, find pred
            if root.left:
                pred = root.left
                steps = 1
                while pred.right and pred.right is not root:
                    pred = pred.right
                    steps += 1
                    
                if not pred.right:
                    curr = curr * 10 + root.val
                    pred.right = root
                    root = root.left

                # otherwise, find go right
                else:
                    if not pred.left: ans += curr
                    for _ in range(steps):
                        curr //= 10
                    pred.right = None
                    root = root.right

            else:
                curr = curr * 10 + root.val
                if not root.right: ans += curr
                root = root.right
                
        return ans
                
                