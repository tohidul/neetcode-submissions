class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0

        if len(prices)==1:
            return max_profit
        
        for i in range(1, len(prices)):
            if prices[i]-min_buy>max_profit:
                max_profit = prices[i]-min_buy
            if prices[i]<min_buy:
                min_buy = prices[i]
        return max_profit
        