class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        mp = {}
        n = len(nums)
        check = n//3
        op=[]
        for i in nums:
            mp[i]=mp.get(i,0)+1
        
        for num,val in mp.items():
            if val > check:
                op.append(num)
        return op
        