class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        mp={0:1}
        pre=0
        res=0
        for i in nums:
            pre+=i
            rem = pre%k
            if rem in mp:
                res+=mp[rem]
            mp[rem] = mp.get(rem,0)+1

        return res
        