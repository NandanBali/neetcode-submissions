class Solution:
    def numDecodings(self, s: str) -> int:
        arr = [-1] * len(s)

        def f(x) -> int:
            if x >= len(s):
                return 1
            
            if arr[x] != -1:
                return arr[x]
            
            if s[x] == "0":
                arr[x] = 0
                return 0
            
            arr[x] = f(x+1)
            if 10 <= int(s[x:x+2]) < 27:
                arr[x] += f(x+2)
            
            return arr[x]
        return f(0)
            