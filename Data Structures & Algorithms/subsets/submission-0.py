class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def _subseq(acc: List[int], index: int):
            if index > len(nums):
                return
            elif index == len(nums):
                self.result.append(acc)
            else:
                _subseq(acc + [nums[index]], index+1)
                _subseq(acc, index+1)
        _subseq([], 0)
        return self.result 