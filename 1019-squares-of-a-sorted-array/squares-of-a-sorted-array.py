class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        res = [num**2 for num in nums]

        res.sort()
        return res
