class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(x, floor) -> int:
            if x == n:
                return 0
            if (x, floor) in memo:
                return memo[(x, floor)]
            elif nums[x] <= floor:
                res = dfs(x+1, floor)
                memo[(x, floor)] = res
                return res
            else:
                res = max(1 + dfs(x+1, nums[x]), dfs(x+1, floor))
                memo[(x, floor)] = res
                return res
        
        fl = -1000
        return dfs(0, fl)