# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "X" 
        return "<" + str(root.val) + ">[" + self.serialize(root.left) + "](" + self.serialize(root.right) + ")"

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "X":
            return None
        r = 0
        while data[r] != ">":
            r += 1
        val = int(data[1:r])
        node = TreeNode(val = val)
        count = 1
        i = r + 1 
        while count > 0:
            i += 1
            if data[i] == "[":
                count += 1
            elif data[i] == "]":
                count -= 1
        left = self.deserialize(data[r+2:i])
        right = self.deserialize(data[i+2:-1])
        node.left = left
        node.right = right
        return node
            