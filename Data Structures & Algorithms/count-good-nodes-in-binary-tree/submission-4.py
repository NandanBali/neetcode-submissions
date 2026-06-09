# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root, root.val))
        res = 0
        while len(q) > 0:
            x, max_val = q.pop()
            if x.val >= max_val:
                res += 1
            if x.left:
                q.append((x.left, max(max_val, x.val)))
            if x.right:
                q.append((x.right, max(max_val, x.val)))
        return res
        