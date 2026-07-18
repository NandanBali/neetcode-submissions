# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        hashes = {}
        nh = hash(None)
        def rechash(node) -> str:
            if not node:
                return str(nh)
            if node in hashes:
                return hashes[node]
            hashes[node] = str(hash(node.val)) + rechash(node.left) + rechash(node.right)
            return hashes[node]
        
        sh =rechash(subRoot)
        def dfs(node) -> bool:
            if not node:
                return sh == nh
            if rechash(node) == sh:
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)


        
