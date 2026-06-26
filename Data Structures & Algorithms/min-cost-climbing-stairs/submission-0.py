class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [-1] * len(cost)
        arr[0] = cost[0]
        arr[1] = cost[1]

        def f(x):
            if arr[x] != -1:
                return arr[x]
            res = min(f(x-1)+cost[x], f(x-2)+cost[x])
            arr[x] = res
            return res
        
        x = len(cost) - 1
        return min(f(x-1), f(x))