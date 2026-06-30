class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coins.reverse()
        arr = [0] * (amount + 1)

        def dfs(r) -> int:
            if arr[r]  != 0:
                return arr[r]
            
            if r == 0:
                return 0

            ec = [c for c in coins if c <= r]
            if len(ec) == 0:
                arr[r] = -1
                return -1

            q = 100000
            for c in ec:
                res = dfs(r-c)
                if res < 0: continue
                q = min(q, 1+res)
            if q == 100000:
                arr[r] = -1
                return -1
            arr[r] = q
            return q
        
        return dfs(amount)