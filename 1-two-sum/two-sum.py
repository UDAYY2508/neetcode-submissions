class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = {}

        for i in range(len(nums)):
            tar = target-nums[i]
            if tar in seen:
                return i,seen[tar]
            seen[nums[i]]=i
