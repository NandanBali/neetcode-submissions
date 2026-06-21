class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.count = 0
        traversed = set()
        nx = len(grid[0])
        ny = len(grid)
        def dfs(x, y):
            if not (0 <= x < nx and 0 <= y < ny):
                return False
            if grid[y][x] == 0:
                return False
            
            traversed.add((x,y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x+dx, y+dy) not in traversed:
                    if not dfs(x+dx, y+dy):
                        self.count += 1
            return True

        for i in range(0, nx):
            for j in range(0, ny):
                if grid[j][i] != 0:
                    dfs(i, j)
                if traversed: break
            if traversed: break 
        return self.count