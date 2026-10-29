class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        

        mp={}
        n = len(nums)
        for i in nums:
            mp[i] = mp.get(i,0)+1
        maxx=0
        for val in nums:
            if mp[val] > n//2:
                res=val
        return res 
