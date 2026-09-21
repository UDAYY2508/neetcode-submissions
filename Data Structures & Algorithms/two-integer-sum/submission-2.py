class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for i in range(len(nums)):
            check = target - nums[i]
            if check in mp:
                return [mp[check],i]
            mp[nums[i]] = i
