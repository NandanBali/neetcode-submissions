# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a, b = deque(), deque()
        a.append(p)
        b.append(q)

        while len(a) and len(b):
            x = a.popleft()
            y = b.popleft()

            if not x and not y:
                return True
            elif x and y and x.val == y.val:
                if x.left and y.left:
                    a.append(x.left)
                    b.append(y.left)
                else:
                    if not (not x.left and not y.left):
                        return False
                if x.right and y.right:
                    a.append(x.right)
                    b.append(y.right)
                else:
                    if not (not x.right and not y.right):
                        return False
            else:
                return False
        return len(a) == 0 and len(b) == 0
