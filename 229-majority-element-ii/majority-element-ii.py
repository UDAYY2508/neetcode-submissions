class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        nums.sort()
        chk = n//3
        count =0 
        op=[]
        prev=nums[0]
        for i in nums:
            if i != prev:
                if chk<count:
                    op.append(prev)
                count=1
            else:
                count+=1

            prev=i
        if chk < count:
            op.append(prev)
        return op
            
                 


