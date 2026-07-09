class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            maxP = max(maxP, prices[sell] - prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
        return maxP