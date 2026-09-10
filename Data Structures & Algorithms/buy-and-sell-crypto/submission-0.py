class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0
        
        # go through each index automatically, no incrementing required
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                # do NOT want to add ONE, if r is far away.
                # l +=1

                # should go to where ever the lowest value in r is
                l = r
            else:
                profit = max(profit, prices[r]-prices[l])
        return profit
            