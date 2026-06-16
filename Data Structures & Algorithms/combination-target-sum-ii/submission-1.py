class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result = []
        def _backtrack(start: int, rolling_sum: int, acc: List[int]):
            if rolling_sum > target:
                return
            elif rolling_sum == target:
                self.result.append(list(acc))
                return
            else:
                s = set()
                for idx, n in enumerate(candidates[start:]):
                    if n in s: continue
                    s.add(n)
                    acc.append(n)
                    _backtrack(start+idx+1, rolling_sum+n, acc)
                    acc.pop()
        _backtrack(0, 0, [])
        return self.result