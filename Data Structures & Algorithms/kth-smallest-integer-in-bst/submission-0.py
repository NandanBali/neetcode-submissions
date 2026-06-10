# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root, 0))
        lst = [0]
        while len(q) > 0:
            x, d = q.pop()
            if x.left:
                d_l = x.left.val - x.val + d
                q.append((x.left, d_l))
                lst.append(d_l)
            if x.right:
                d_r = x.right.val - x.val + d
                q.append((x.right, d_r))
                lst.append(d_r)
        lst.sort()
        return lst[k-1] + root.val
            