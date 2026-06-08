# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _length(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self._length(root.left), self._length(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        c1 = abs(self._length(root.left) - self._length(root.right) )
        if c1 > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)       