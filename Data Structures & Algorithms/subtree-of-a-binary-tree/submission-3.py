# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.found = False
        def _hashNode(node: Optional[TreeNode], check_match: bool, target_hash):
            if not node:
                return hash(None)
            left_hash = _hashNode(node.left, check_match, target_hash)
            right_hash = _hashNode(node.right, check_match, target_hash)

            current_hash = hash((node.val, left_hash, right_hash))

            if check_match and target_hash:
                if current_hash == target_hash:
                    self.found = True
            return current_hash

        target_hash = _hashNode(subRoot, False, None)
        _hashNode(root, True, target_hash)
        return self.found
