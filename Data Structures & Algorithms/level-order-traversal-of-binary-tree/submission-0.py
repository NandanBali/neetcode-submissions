# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        lst: List[List[int]] = []
        while len(q) > 0:
            x, level = q.popleft()
            if x:
                if len(lst) > level:
                    lst[level].append(x.val)
                else:
                    lst.append([x.val])
                    print(f"{x.val} -> {lst}")
                q.append((x.left, level+1))
                q.append((x.right, level+1))
        return lst