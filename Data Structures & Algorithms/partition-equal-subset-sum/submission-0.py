class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        for num in nums:
            s += num
        if s % 2 == 1:
            return False
        nums.sort(reverse=True)
        cache = {}

        def dfs(s1: int, s2: int, rs: int, idx) -> bool:
            if abs(s1-s2) > rs:
                return False
            elif rs == 0:
                return s1 == s2
            
            if (abs(s1-s2), rs) in cache:
                return cache[(abs(s1-s2), rs)]
            res = dfs(s1+nums[idx], s2, rs - nums[idx], idx+1) or dfs(s1, s2+nums[idx], rs-nums[idx], idx+1)
            cache[(abs(s1-s2), rs)] = res
            return res
        
        return dfs(0, 0, s, 0)