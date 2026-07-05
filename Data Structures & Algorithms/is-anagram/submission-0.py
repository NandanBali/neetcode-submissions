class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lset = {}
        for l in s:
            if l not in lset:
                lset[l] = 0
            lset[l] += 1
        
        for l in t:
            if l not in lset:
                return False
            if lset[l] > 0:
                lset[l] -= 1
            else:
                return False
        
        for val in lset.values():
            if val != 0:
                return False
            
        return True