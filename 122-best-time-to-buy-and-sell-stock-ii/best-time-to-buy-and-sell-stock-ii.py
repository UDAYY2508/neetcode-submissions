class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        nums = prices
        max_profit=0
        w = 0
        for r in range(1,len(nums)):
            profit=0
            if nums[w]>nums[r]:
                w+=1
            elif nums[r]>nums[w]:
                profit = nums[r]-nums[w]
                max_profit+=profit
                w+=1
                r+=1
            elif nums[r] == nums[w]:
                w+=1
                r+=1
            r+=1
        return max_profit
