# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _maxlen(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self._maxlen(node.left), self._maxlen(node.right))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self._maxlen(root.right) + self._maxlen(root.left), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))