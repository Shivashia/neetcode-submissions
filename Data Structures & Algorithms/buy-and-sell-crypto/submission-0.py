class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice=prices[0]
        for i in range(1,len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            profit = max(profit, prices[i]-buyPrice)
        return profit