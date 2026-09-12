class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        n = len(nums)

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1

        for key,val in count.items():
            if val > n/2:
                return key 