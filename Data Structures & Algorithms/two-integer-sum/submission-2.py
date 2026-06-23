class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            d = target - n
            if d in prevMap:
                return [prevMap[d], i]
            prevMap[n] = i