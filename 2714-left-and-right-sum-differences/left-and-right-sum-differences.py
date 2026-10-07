class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        lfir=0
        rfir=0
        lsum=[]*len(nums)
        rsum=[]*len(nums)
        res=[]

        for i in range(len(nums)):
            lsum.append(lfir)
            lfir+=nums[i]
        for i in range(len(nums)-1,-1,-1):
            rsum.append(rfir)
            rfir+=nums[i]
        rsum=rsum[::-1]

        for i in range(len(nums)):
            res.append(abs(lsum[i]-rsum[i]))
        return res
        

