class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        

        curMin = prices[0]
        maxpro = 0

        for i in prices:
            
            profit = i - curMin
            if profit > maxpro:
                maxpro = profit
            curMin = min(curMin,i)
        return maxpro