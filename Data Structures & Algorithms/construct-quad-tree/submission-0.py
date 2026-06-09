"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 0:
            return Node()
        v1 = grid[0][0]
        isLeaf = True
        for row in grid:
            for col in row:
                if col != v1:
                    isLeaf = False
                    break
            if not isLeaf:
                break
        
        if isLeaf:
            return Node(val=(v1 == 1), isLeaf=True)
        else:
            n = len(grid) // 2
            s1 = self.construct([row[:n] for row in grid[:n]])
            s2 = self.construct([row[n:] for row in grid[:n]])
            s3 = self.construct([row[:n] for row in grid[n:]])
            s4 = self.construct([row[n:] for row in grid[n:]])
            return Node(val = False, isLeaf=False, topLeft=s1, topRight=s2, bottomLeft=s3, bottomRight=s4)
             