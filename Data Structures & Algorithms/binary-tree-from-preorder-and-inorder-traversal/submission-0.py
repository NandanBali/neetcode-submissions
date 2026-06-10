# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        n = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        if len(preorder) == 1:
            return node
        inorder_left = inorder[:n]
        preorder_left = preorder[1:(n+1)]
        node.left = self.buildTree(preorder_left, inorder_left)
        inorder_right = inorder[(n+1):]
        preorder_right = preorder[(n+1):]
        node.right = self.buildTree(preorder_right, inorder_right)
        return node