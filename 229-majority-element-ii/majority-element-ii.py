class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        chk = n//3
        op =[]
        mp = {}
        for i in nums:
            mp[i]=mp.get(i,0)+1
        for num,val in mp.items():
            if val>chk:
                op.append(num)
        return op