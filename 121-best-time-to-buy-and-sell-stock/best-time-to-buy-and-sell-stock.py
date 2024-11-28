class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]  # Initialize min_price with the first price
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit