class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sn = sum(nums)
        if sn % 2:
            return False
        target = sn // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for w in nums:
            for j in range(target, w - 1, -1):
                dp[j] |= dp[j - w]
            if dp[target]:
                return True
        return dp[target]