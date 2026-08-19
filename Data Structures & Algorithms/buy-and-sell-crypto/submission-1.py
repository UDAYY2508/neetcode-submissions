class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0 
        minn = prices[0]

        for i in range(len(prices)):
            cur = prices[i] - minn
            minn = min(prices[i],minn)
            if cur > best:
                best = cur
        return best 

       
        
            

            