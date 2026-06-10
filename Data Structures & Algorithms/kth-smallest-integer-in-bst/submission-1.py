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
        
        self.iter = 0
        self.min_val = root.val
        self.res = root.val
        def _inorder_traversal(node: TreeNode):
            if node.left:
                _inorder_traversal(node.left)
            
            if node.val < self.min_val:
                self.min_val = node.val
                self.iter = 1
            else:
                self.iter += 1
            
            if self.iter == k:
                self.res = node.val
                return
            
            if node.right:
                _inorder_traversal(node.right)
        _inorder_traversal(root)
        return self.res