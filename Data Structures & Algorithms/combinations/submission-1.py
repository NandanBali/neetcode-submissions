class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        def _backtrack(acc: List[int], start: int):
            if len(acc) == k:
                self.result.append(list(acc))
                return
            
            for i in range(start, n+1):
                acc.append(i)
                _backtrack(acc, i+1)
                acc.pop()
        _backtrack([], 1)
        return self.result