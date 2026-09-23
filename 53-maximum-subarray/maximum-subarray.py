class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_ = float("-inf")
        summ = 0

        for i in nums:
            summ+=i
            max_=max(max_,summ)
            if summ<0:
                summ=0
        return max_