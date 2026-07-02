class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * n for _ in range(0, m)]
        cache[m-1][n-1] = 1

        def f(x, y) -> int:
            if y == m or x == n:
                return 0
            if cache[y][x] != -1:
                return cache[y][x]
            
            cache[y][x] = f(x+1, y) + f(x, y+1)
            return cache[y][x]
        
        return f(0, 0)