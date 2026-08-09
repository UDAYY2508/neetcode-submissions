class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        con = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in con:
                return [con[diff],i]
            con[nums[i]] = i 
            

        
                 