class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prefix = [ 0]
        for num in nums:
            prefix.append(num + prefix[-1])
        
        best = float('-inf')
        n = len(nums)
        for i in range(0, n): 
            for l in range(1, n - i + 1):
                best = max(best, prefix[i + l] - prefix[i])
        return int(best)