class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        copy=nums[:]
        res=[]
        nums.sort()
        mp = {}
        nums=nums[::-1]
        
        for i in range(len(nums)):
            j=i+1
            curr=nums[i]
            count=0
            while j<len(nums):
                if nums[j]<curr:
                    count+=1
                    j+=1
                else:
                    j+=1
            mp[curr]=count
        for num in copy:
            res.append(mp[num])
            
        return res
                    
                
