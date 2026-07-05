class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for idx, n in enumerate(nums):
            if target - n in hset:
                return [hset[target-n], idx]
            hset[n] = idx
        
        return [0, 0]