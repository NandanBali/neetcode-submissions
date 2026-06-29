class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in s]
        
        def check(x, y):
            if x == y:
                dp[x][y] = 1 
                return True
            elif x+1 == y:
                r = s[x] == s[y]
                if r: dp[x][y] = 1
                else: dp[x][y] = -1
                return r
            else:
                if s[x] != s[y]:
                    dp[x][y] = -1
                    return False
                if dp[x][y] != 0:
                    return dp[x][y] == 1
                dp[x][y] = check(x+1, y-1)
                return dp[x][y]
                 
        res = 0
        for st in range(0, len(s)):
            for l in range(0, len(s)):
                if st + l >= len(s): break
                if check(st, st+l): res += 1 

        return res