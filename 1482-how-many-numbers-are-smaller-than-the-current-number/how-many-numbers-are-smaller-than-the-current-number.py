class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        temp = sorted((nums))
        mp={}

        for i,n in enumerate(temp):
            if n not in mp:
                mp[n]=i
        res=[]

        for i in nums:
            res.append(mp[i])
        return res
          