class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        
        mp={}
        n=len(nums)
        for i in nums:
            mp[i] = mp.get(i,0)+1
        
        for i,v in mp.items():
            if v >=2:
                nums.append(i)
        
        return nums[n:]