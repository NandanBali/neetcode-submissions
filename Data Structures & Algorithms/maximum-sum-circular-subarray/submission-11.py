class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        rmax = [0] * n
        rmax[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            rmax[i] = max(rmax[i + 1], suffix_sum)
        
        max_sum = nums[0]
        cur_max = 0
        prefix_sum = 0
        
        for i in range(0, n):
            cur_max = max(cur_max + nums[i], nums[i])
            max_sum = max(max_sum, cur_max)
            prefix_sum += nums[i]

            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + rmax[i + 1])
        
        return max_sum