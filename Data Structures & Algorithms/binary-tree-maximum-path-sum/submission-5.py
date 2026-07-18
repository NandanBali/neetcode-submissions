# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001
        @cache
        def dfs(node) -> tuple[int, int]:
            if not node:
                return (0, 0) 
            inc = max(node.val + max(dfs(node.left)[0], dfs(node.right)[0]), node.val)
            exc = max(node.val + dfs(node.left)[0] + dfs(node.right)[0], inc)
            self.res = max(self.res, exc) 
            return (inc, exc)
        r = dfs(root)
        self.res = max(self.res, r[1])
        return self.res