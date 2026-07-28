class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for t in range(1, amount + 1):
            for index, coin in enumerate(coins):
                if t < coin:
                    dp[t][index+1] = dp[t][index]
                    continue 
                dp[t][index + 1] += dp[t-coin][index + 1] + dp[t][index]
        
        return dp[amount][len(coins)]