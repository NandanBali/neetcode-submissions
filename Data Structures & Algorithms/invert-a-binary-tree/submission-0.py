# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inplace(node: Optional[TreeNode]):
            if node:
                t = node.left
                node.left = node.right
                node.right = t
                inplace(node.left)
                inplace(node.right)
            else:
                return
        inplace(root)
        return root
