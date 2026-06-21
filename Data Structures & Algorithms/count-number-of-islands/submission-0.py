class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        traversed = set()
        xl = len(grid[0])
        yl = len(grid)
        def dfs(x, y):
            if not (0 <= x < xl and 0 <=y < yl) or grid[y][x] == "0" or (x,y) in traversed:
                return False 
            traversed.add((x,y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(x+dx, y+dy)
            return True
        
        count = 0
        for i in range(0, xl):
            for j in range(0, yl):
                if grid[j][i] == "0" or (i, j) in traversed:
                    continue
                dfs(i, j)
                count += 1
        
        return count