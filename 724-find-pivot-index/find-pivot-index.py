class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        

        ltot=0
        tot = sum(nums)

        for i in range(len(nums)):
            rtot = tot - ltot - nums[i]

            if ltot == rtot:
                return i
            ltot+=nums[i] 
        return -1