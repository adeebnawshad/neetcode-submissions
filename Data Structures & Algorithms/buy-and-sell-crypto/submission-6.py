class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = 0
        for sell in range(1, len(prices)):
            maxP = max(maxP, (prices[sell] - prices[buy]))
            if prices[sell] < prices[buy]:
                buy = sell
        return maxP