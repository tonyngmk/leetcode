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
            # Start with left
            if root.left:
                pred = root.left
                steps = 1
                while pred.right and pred.right is not root:
                    pred = pred.right
                    steps += 1
                    
                # Create link
                if not pred.right:
                    curr = curr * 10 + root.val
                    pred.right = root
                    root = root.left

                # Break link
                else:
                    if not pred.left: ans += curr
                    for _ in range(steps): curr //= 10
                    pred.right = None
                    root = root.right

            # Reached the leftmost
            else:
                curr = curr * 10 + root.val
                if not root.right: ans += curr
                root = root.right
                
        return ans
