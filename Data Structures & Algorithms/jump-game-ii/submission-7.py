class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        n = len(nums)
        count = 0
        while l < n - 1:
            count += 1
            best = 0
            best_index = l
            for i in range(l, l + nums[l] + 1):
                if i == n - 1:
                    return count
                if i - l + nums[i] >= best:
                    best_index = i
                    best = i - l + nums[i]
            l = best_index
        return count
            
