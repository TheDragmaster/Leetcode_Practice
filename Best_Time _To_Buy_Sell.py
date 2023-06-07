class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Left = Buy.    Right = Sell\
        maxp = 0

        while r < len(prices):
            # Profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp
