class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0
        for i in numset:

            if i - 1 not in numset:
                current = 1
                x = i                

                while x + 1 in numset:
                    x+=1
                    current += 1

                longest = max(longest,current)

        return longest 
