class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        pre = 0
        con = 0

        for i in nums:
            pre += i
            if pre - k in mp:
                con += mp[pre-k]
            mp[pre] = mp.get(pre,0)+1
        return con

            