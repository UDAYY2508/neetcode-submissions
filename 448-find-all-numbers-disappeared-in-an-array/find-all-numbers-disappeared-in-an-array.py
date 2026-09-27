class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        res = []
        con = set(nums)
        for i in range(1,n+1):
            if i not in con:
                res.append(i)
        return res
