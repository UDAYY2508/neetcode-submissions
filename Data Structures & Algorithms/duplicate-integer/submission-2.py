class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        con = set(nums)

        if len(con) != len(nums):
            return True
        else:
            return False
