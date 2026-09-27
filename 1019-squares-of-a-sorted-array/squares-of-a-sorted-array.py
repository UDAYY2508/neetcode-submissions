class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res=[]
        l=0
        r=len(nums)-1
        while l<=r:
            curR=nums[r]**2
            curL=nums[l]**2
            if curR<curL:
                res.append(curL)
                l+=1
            else:
                res.append(curR)
                r-=1
        return res[::-1]
            

