class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy,sell = 0, 1

        while(sell < len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell]-prices[buy]
                res = max(res,profit)
            sell +=1
        return res