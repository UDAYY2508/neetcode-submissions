class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        mp={0:1}
        p=0
        c=0
        for i in nums:
            p+=i
            rem = p%k
            if rem in mp:
                c+=mp[rem]    
            mp[rem]=mp.get(rem,0)+1            
        return c
