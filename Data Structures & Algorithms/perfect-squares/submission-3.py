class Solution:
    def numSquares(self, n: int) -> int:
        cache = [-1] * (n+1)
        cache[0] = 0
        cache[1] = 1
        def dfs(x, count) -> int:
            if cache[x] >= 0:
                return cache[x] 
            
            res = 4
            if count > 5:
                return res + 1

            for i in range(1, math.floor(math.sqrt(x)) + 2):
                if i * i > x:
                    break
                res = min(res, 1 + dfs(x-(i*i), count+1))
            cache[x] = res
            return res
        return dfs(n, 0)