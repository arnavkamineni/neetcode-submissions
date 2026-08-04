class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minPrice = prices[0]
        profit = 0
        for i in range(n):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i] - minPrice)
        
        return max(0, profit)
            
