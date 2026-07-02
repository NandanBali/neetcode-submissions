class Solution:
    def integerBreak(self, n: int) -> int:
        if 1 < n < 4:
            return n - 1

        tc = [-1] * (n+1)
        tc[0], tc[1] = 1, 1

        def optimal(x) -> int:
            if tc[x] > 0:
                return tc[x]
            res = 0
            for i in range(1, x+1):
                tc[x-i] = optimal(x-i)
                res = max(i * tc[x-i], res)
            tc[x] = res
            return res
        
        return optimal(n)