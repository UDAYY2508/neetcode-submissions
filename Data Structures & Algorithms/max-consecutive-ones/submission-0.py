class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0 
        i = 0
        maxx = 0

        while i <len(nums):
            if nums[i] != 0:
                count +=1
            else:
                count = 0
            maxx = max(maxx,count)
            i+=1
        return maxx
            


        

            