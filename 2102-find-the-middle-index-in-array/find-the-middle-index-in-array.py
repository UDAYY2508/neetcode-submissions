class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        
        ltot =0
        rtot =0 
        tot =sum(nums)

        for i in range(len(nums)):
            rtot = tot-ltot-nums[i]

            if rtot == ltot:
                return i

            ltot+=nums[i]
        return -1
        