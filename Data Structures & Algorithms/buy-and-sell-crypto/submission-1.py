class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1, 0, -1):
            profit = prices[i] - min(prices[0: i])
            result = max(result, profit)
        return result