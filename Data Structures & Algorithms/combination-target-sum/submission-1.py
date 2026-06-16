class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def _sum(l: List[int]):
            s = 0
            for a in l: s += a
            return s
        
        self.result = []

        def _combinations(acc: List[int], pool: List[int]):
            if _sum(acc) == target:
                self.result.append(list(acc))
                return
            elif _sum(acc) > target:
                return
            else:
                for index, n in enumerate(pool):
                    _combinations(acc+[n], pool[index:])
        _combinations([], nums)
        return self.result