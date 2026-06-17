class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def backtrack(acc, freq):
            if len(acc) == len(nums):
                self.result.append(list(acc))
                return
            
            for key, value in freq.items():
                if value > 0:
                    freq[key] -= 1
                    acc.append(key)
                    backtrack(acc, freq)
                    acc.pop()
                    freq[key] += 1
        backtrack([], Counter(nums))
        return self.result