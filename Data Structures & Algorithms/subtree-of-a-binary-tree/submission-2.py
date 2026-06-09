# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def _serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "$"
            return str(node.val) + _serialize(node.left) + _serialize(node.right)

        root_ser = _serialize(root)
        subroot_ser = _serialize(subRoot)

        return subroot_ser in root_ser
     