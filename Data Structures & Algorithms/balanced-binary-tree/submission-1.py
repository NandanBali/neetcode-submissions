# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _get_length(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self._get_length(node.left)
        right = self._get_length(node.right)
        if left < 0 or right < 0:
            return -1

        if abs(left-right) > 1:
            return -1

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self._get_length(root) < 0:
            return False
        return True