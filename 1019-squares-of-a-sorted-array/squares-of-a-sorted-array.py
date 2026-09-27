class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if not nums:
            return nums
        
        if nums[0]>0:
            return [num**2 for num in nums]

        res=[0]*len(nums)
        l=0
        r=len(nums)-1
        i=r
        while l<=r:
            curR=nums[r]**2
            curL=nums[l]**2
            if curR<curL:
                res[i]=curL
                i-=1
                l+=1
            else:
                res[i]=curR
                i-=1
                r-=1
        return res
            

