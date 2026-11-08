class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        con = set(nums)
        return len(con) != len(nums)