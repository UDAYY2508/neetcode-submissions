class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        lnums = []
        mul=1
        for i in range(len(nums)):
            lnums.append(mul)
            mul = nums[i]*mul
        rnums = []
        mul=1
        nums = nums[::-1]
        for i in range(len(nums)):
            rnums.append(mul)
            mul =nums[i]*mul
        rnums = rnums[::-1]
        res= []

        for i in range(len(nums)):
            res.append(lnums[i]*rnums[i])
        return res

        
