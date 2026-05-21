class Solution:
    def isValid(self, s: str) -> bool:
        bc = [''] * 1000
        n = 0
        for b in s:
            if b== "[" or b== "(" or b== "{":
                bc[n] = b 
                n += 1
            else:
                if (b == ")" and bc[n-1] == "(") or (b == "]" and bc[n-1] == "[") or (b=="}" and bc[n-1] == "{"):
                    n -= 1
                else:
                    return False
        return n == 0