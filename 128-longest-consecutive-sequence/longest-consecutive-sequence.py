class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        seen=set(nums)
        max_=0
        
        for i in seen:
            curr=i
            l=0
            if curr-1 not in seen:
                while curr in seen:
                    l+=1
                    curr+=1
                max_=max(max_,l)

        return max_

