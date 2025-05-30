class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #TC: O(n) SC: O(1)
        mp = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                mp += prices[i] - prices[i - 1]
        return mp