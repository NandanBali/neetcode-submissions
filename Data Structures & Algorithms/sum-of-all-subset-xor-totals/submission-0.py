class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.sum = 0
        def _count(acc: List[int], index: int):
            if index > len(nums):
                return
            elif index == len(nums):
                r = 0
                for n in acc:
                    r = r ^ n
                self.sum += r
                return
            else:
                acc.append(nums[index])
                _count(acc, index+1)
                acc.pop()
                _count(acc, index+1)
        _count([], 0)
        return self.sum
                  

            