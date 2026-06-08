# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        while len(q) > 0:
            x = q.pop()
            if x:
                t = x.left
                x.left = x.right
                x.right = t
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return root
        