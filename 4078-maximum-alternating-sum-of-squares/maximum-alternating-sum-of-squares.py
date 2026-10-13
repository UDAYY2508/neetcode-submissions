class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sqr=[]
        op=0
        for n in nums:
            sq = n**2
            sqr.append(sq)

        sqr.sort()
        sqrL=len(sqr)
        mid = sqrL//2
        larr=sqr[:mid]
        rarr=sqr[mid:]

        
        for i in range(len(larr)):
            op-=larr[i]
        for i in range(len(rarr)):
            op+=rarr[i]
        

        return op