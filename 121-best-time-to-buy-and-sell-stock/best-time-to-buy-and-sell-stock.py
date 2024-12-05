class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minP = prices[0]
        profit = 0

        for p in prices[0:]:
            profit = max(profit, (p - minP))
            minP = min(minP, p)
        return profit 