# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(preorder[0])]
        post_index = 0

        for val in preorder[1:]:
            node = TreeNode(val)

            # leaf node / completed
            while stack[-1].val == postorder[post_index]:
                stack.pop()
                post_index += 1

            # not completed, add left first before right
            if not stack[-1].left: stack[-1].left = node
            else: stack[-1].right = node

            stack.append(node)

        return stack[0]