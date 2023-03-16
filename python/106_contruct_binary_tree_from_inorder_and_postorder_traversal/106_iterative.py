# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_map = {v:k for k, v in enumerate(inorder)} 
        
        for i in range(len(postorder)-2, -1, -1):
            
            val = postorder[i]
            node = TreeNode(val)
            
            if inorder_map[val] > inorder_map[stack[-1].val]: stack[-1].right = node
            else:
                while stack and inorder_map[val] < inorder_map[stack[-1].val]:
                    parent = stack.pop()
                parent.left = node
            stack.append(node)
            
        return root