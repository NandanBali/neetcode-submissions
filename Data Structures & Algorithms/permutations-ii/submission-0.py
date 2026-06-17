class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _backtrack(lst) -> List[List[int]]:
            if len(lst) == 1:
                return [lst]
            
            a = lst[0]
            res: List[List[int]] = _backtrack(lst[1:])
            s: set[tuple[int, ...]] = set()
            for l in res:
                for i in range(0,len(l)+1):
                    l.insert(i, a)
                    s.add(tuple(l))
                    del l[i]
            return [list(a) for a in s]
        return _backtrack(nums)
