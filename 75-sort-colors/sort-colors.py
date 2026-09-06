class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        i = 0
        j = len(nums)-1

        while i<=j:
            if nums[i] == 1:
                i+=1
            elif nums[i] == 0:
                nums[write],nums[i] =  nums[i],nums[write]
                write+=1
                i+=1
            else:
                nums[j],nums[i] =  nums[i],nums[j]
                j-=1
                  
        return nums
            