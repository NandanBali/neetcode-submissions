# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((a,b))

        while len(q) > 0:
            x, y = q.popleft()
            if not x and not y:
                continue
            elif x and y and x.val == y.val:
                q.append((x.left, y.left))
                q.append((x.right, y.right))
            else:
                return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot

        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    