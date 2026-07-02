class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])

        cache = [[-1] * ncols for _ in range(0, nrows)]
        cache[nrows-1][ncols-1] = grid[nrows-1][ncols-1]
        infinity = 100000
        def dfs(x, y) -> int:
            if x == ncols or y == nrows:
                return infinity

            if cache[y][x] >= 0:
                return cache[y][x]
            
            cache[y][x] = grid[y][x] + min(dfs(x+1, y), dfs(x, y+1))
            return cache[y][x]
        return dfs(0, 0)