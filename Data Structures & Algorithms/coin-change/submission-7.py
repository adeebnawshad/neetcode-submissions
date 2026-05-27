class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # c itself + dp[a - c] (can be multiple possible such as 1 + dp[5] or 3 + dp[3] or 4 + dp[2] for 7 so we need to take the minimum)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
