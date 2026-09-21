class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        
        mp = {}

        for i in nums:
            mp[i] = mp.get(i,0)+1
        for num,val in mp.items():
            if val == 1:
                return num
