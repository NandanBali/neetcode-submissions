# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        self.pos = {}
        for idx, val in enumerate(inorder):
            self.pos[val] = idx
        
        self.pre_idx = 0
        def _dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            root_val: int = preorder[self.pre_idx]
            self.pre_idx += 1
            n = self.pos[root_val]
            node = TreeNode(val=root_val)
            node.left = _dfs(l, n-1)
            node.right = _dfs(n+1, r)
            return node
        return _dfs(0, len(inorder)-1)