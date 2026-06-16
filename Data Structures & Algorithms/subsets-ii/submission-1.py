class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []

        def _backtrack(acc, index, exclude: set[int]):
            if index == len(nums):
                self.result.append(list(acc))
                return

            if not nums[index] in exclude:
                acc.append(nums[index])
                _backtrack(acc, index+1, set(exclude))
                acc.pop()
            exclude.add(nums[index])
            _backtrack(acc, index+1, set(exclude))

        _backtrack([], 0, set())
        return self.result