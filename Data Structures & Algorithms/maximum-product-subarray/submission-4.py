class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg_max = 0
        pos_max =  nums[0]
        ncmax = nums[0]

        for num in nums[1:]:
            c = (num * neg_max, num * pos_max, num)
            neg_max = min(c)
            pos_max = max(c)
            ncmax = max(pos_max, ncmax)
        return ncmax