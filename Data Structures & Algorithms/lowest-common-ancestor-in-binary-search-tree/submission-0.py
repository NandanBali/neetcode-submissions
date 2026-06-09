# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def _rec_dfs(node: Optional[TreeNode], acc: list[TreeNode], target: int) -> bool:
            if not node:
                return False

            acc.append(node)
            if node.val == target:
                return True
            l_acc, r_acc = [], []

            l = _rec_dfs(node.left, l_acc, target)
            r = _rec_dfs(node.right, r_acc, target)

            if l: acc.extend(l_acc)
            else: acc.extend(r_acc)
            return l or r

        x_acc, y_acc = [], []
        if _rec_dfs(root, x_acc, p.val) and _rec_dfs(root, y_acc, q.val):
            lca = root
            for a,b in zip(x_acc, y_acc):
                if a.val == b.val: lca = a
                else: break
            return lca
        return root