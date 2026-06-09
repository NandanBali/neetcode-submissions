# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append((root, 0))
        lst: List[List[int]] = []
        while len(q) > 0:
            x, level = q.popleft()
            if x:
                if level < len(lst):
                    lst[level].append(x.val)
                else:
                    lst.append([x.val])
                q.append((x.left, level+1))
                q.append((x.right, level+1))
        return list(map(lambda x: x[-1], lst))

                
