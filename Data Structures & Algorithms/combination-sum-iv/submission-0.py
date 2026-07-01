class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        cache = [-1] * (target+1)

        def dfs(cs) -> int:
            if cs == target:
                return 1
            if cache[target - cs] != -1:
                return cache[target - cs]
            
            enums = [n for n in nums if n <= target - cs]
            if len(enums) == 0:
                return 0

            ways = 0
            for num in enums:
                ways += dfs(cs+num)
            cache[target - cs] = ways
            return ways

        return dfs(0)  
            
