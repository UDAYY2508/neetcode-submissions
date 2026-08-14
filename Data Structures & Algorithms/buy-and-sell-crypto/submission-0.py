class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       
        curr = 0
        minn = prices[0]
        best = 0
        for i in prices:
            if i < minn:
                minn = i
            curr = i - minn
            best = max(best,curr)
                
        return best
            

            