class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def _sum(l: List[int]):
            s = 0
            for a in l: s += a
            return s

        self.result = []

        def _combination(acc, pool):
            s = _sum(acc)
            if s > target: return
            elif s == target:
                self.result.append(list(acc))
                return
            else:
                s = set()
                for idx, n in enumerate(pool):
                    if n in s: continue
                    s.add(n)
                    _combination(acc+[n], pool[(idx+1):])
        _combination([], candidates)
        return self.result