class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        cache[0] = 0
        cache[1] = 1
        def dfs(x, count) -> int:
            if x in cache:
                return cache[x] 
            
            res = 4
            if count == res:
                return count
            
            t: int = math.floor(math.sqrt(x)) + 2
            for i in range(1, math.floor(math.sqrt(x)) + 2):
               if i * i > x: break
               res = min(res, 1 + dfs(x-(i*i), count+1))
            cache[x] = res
            return res
        return dfs(n, 0)