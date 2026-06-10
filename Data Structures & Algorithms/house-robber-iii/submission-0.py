# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def _count(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return (0, 0)
            
            res_left = _count(node.left)
            res_right = _count(node.right)

            path_inc = res_left[0] + res_right[0] + node.val
            path_exc = max(res_left[0], res_left[1]) + max(res_right[0], res_right[1])
            return (path_exc, path_inc)
        res = _count(root)
        return max(res[0],res[1])