class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        
        l = 0
        r = 1

        while r<len(nums):
            if nums[l] == nums[r]:
                l+=1
                nums.pop(r)
                r=l
            r+=1
        return nums[l]
