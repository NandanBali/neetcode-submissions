# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node) -> tuple[int, int]:
            if not node:
                return (0, 0)
            nld, nrd = dfs(node.left), dfs(node.right)
            r1 = 1 + max(nld[0], nrd[0])
            r2 = 1 + nld[0] + nrd[0]
            self.res = max(r2, self.res)
            return (r1, r2)
        self.res = max(dfs(root)[1], self.res)
        return self.res - 1
