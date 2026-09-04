class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let res = 0
        let buy = 0
        for (let sell = 0; sell < prices.length; sell++) {
            res = Math.max(prices[sell] - prices[buy], res)
            if (prices[sell] < prices[buy]) {
                buy = sell
            }
        }
        return res
    }
}
