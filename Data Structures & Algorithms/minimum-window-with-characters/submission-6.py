class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_map = {}

        l, r = 0, 0
        n = len(s)
        ct = Counter(t)
        cs = Counter(s)
        for key, val in ct.most_common():
            if not (key in cs and cs[key] >= val):
                return ""

        required = set(ct.keys())
        cw = Counter()
        
        result = str(s)
        for r in range(0, n):
            if s[r] in ct:
                cw[s[r]] += 1
                if cw[s[r]] >= ct[s[r]]:
                    required.discard(s[r])

            while len(required) == 0:
                if len(result) > r - l:
                    result = s[l:r+1]

                if s[l] in ct:
                    cw[s[l]] -= 1
                if cw[s[l]] < ct[s[l]]:
                    required.add(s[l])
                l += 1
        return result

                
