class Solution:
    def longestPalindrome(self, s: str) -> str:
        checked = {}

        def f(x, y) -> bool:
            if (x, y) in checked:
                return checked[(x,y)]    
            if x == y:
                return True
            elif x + 1== y:
                return s[x] == s[y]
            elif s[x] != s[y]:
                return False
            else:
                res = f(x+1, y-1)
                checked[(x,y)] = res
                return res
        
        biggest = s[0]
        for offset in range(1, len(s)):
            for p1 in range(0, len(s) - offset):
                if len(biggest) < offset + 1 and f(p1, p1+offset):
                    biggest = s[p1: p1+offset+1]
        return biggest
                    

       