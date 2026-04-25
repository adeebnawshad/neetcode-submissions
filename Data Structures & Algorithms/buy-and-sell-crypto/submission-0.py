class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        sellDay = len(prices) - 1
        while (sellDay >= 1):
            buyDay = sellDay - 1
            while (buyDay >= 0):
                if prices[sellDay] - prices[buyDay] > maxProfit:
                    maxProfit = prices[sellDay] - prices[buyDay]
                buyDay -= 1
            sellDay -= 1
        return maxProfit        
