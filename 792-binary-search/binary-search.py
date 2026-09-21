class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        l =0
        r =len(nums)-1
        i = r//2
        while l<=r:
            i = l+r-1//2
            if target>nums[i]:
                l = i+1
            elif target<nums[i]:
                r =i-1
            else:
                return i
        return -1
