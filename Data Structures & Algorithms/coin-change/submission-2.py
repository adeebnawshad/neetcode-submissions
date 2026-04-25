class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = 1e9
            for coin in coins:
                if coin <= amount:
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res
        minCount = dfs(amount)
        return -1 if minCount >= 1e9 else minCount
