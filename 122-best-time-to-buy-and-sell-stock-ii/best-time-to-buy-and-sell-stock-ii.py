class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        max_profit=0
        w = 0
        for r in range(1,len(prices)):
            profit=0
            if prices[w]>prices[r]:
                w+=1
            elif prices[r]>prices[w]:
                profit = prices[r]-prices[w]
                max_profit+=profit
                w+=1
                r+=1
            elif prices[r] == prices[w]:
                w+=1
                r+=1
            r+=1
        return max_profit
