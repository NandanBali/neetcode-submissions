class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        maxn = float('-inf')
        for num in nums:
            prev = max(num, prev + num)
            maxn = max(prev, maxn)
        return int(maxn)
