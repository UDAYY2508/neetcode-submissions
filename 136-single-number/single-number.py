class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        
        x=nums[0]
        for n in nums[1:]:
            x^=n
        return x