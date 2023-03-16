# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Inorder pinpoints which is the node
        # Preorder splits group of nodes to its left and right subtree
        
        if not preorder: return None
        
        inorder_map = {v:k for k, v in enumerate(inorder)}
        
        root = TreeNode(preorder[0]) # Create root
        stack = [root]
        
        for i in range(1, len(preorder)):
            val = preorder[i]
            node = TreeNode(val)
            
            # If inorder position of current is lesser than top of stack, it is at it's left
            if inorder_map[val] < inorder_map[stack[-1].val]:
                stack[-1].left = node
                
            else:
                while stack and inorder_map[val] > inorder_map[stack[-1].val]: # Find the closest node to the left of curr
                    parent = stack.pop()
                parent.right = node 
            stack.append(node)
            
        return root
        