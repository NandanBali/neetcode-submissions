# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isvalid(node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if not node:
                return True
            # check constraints
            if min_val < node.val < max_val:
                return _isvalid(node.left, min_val, node.val) and _isvalid(node.right, node.val, max_val)
            else:
                return False
        return _isvalid(root, min_val=float('-inf'), max_val=float('inf'))
        