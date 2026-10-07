class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mp={0:1}
        res=0
        pre=0
        for i in nums:
            pre+=i
            diff = pre-k
            if diff in mp:
                res+=mp[diff]

            mp[pre]=mp.get(pre,0)+1
        return res