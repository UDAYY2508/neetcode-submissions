class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
            con = set(nums)
            long = 0

            for i in nums:
                if i - 1 not in con:
                    curr = i
                    count = 1
                    while curr + 1 in con:
                        count += 1
                        curr += 1
                    long = max(long,count)

            return long
                    