class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        for sell in range(1, len(prices)):
            res = max(res, prices[sell] - prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell
        return res