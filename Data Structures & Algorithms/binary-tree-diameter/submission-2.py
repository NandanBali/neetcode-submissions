# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def get_length(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_len = get_length(node.left)
            right_len = get_length(node.right)

            self.max_diameter = max(left_len+right_len, self.max_diameter)
            return 1 + max(left_len, right_len)
        
        get_length(root)
        return self.max_diameter