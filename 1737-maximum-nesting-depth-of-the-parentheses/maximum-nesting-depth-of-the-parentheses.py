class Solution:
    def maxDepth(self, s: str) -> int:
        
        
        max_c=0
        count=0
        for i in s:
            if i== "(":
                count+=1
                max_c=max(max_c,count)
            elif i== ")":
                count-=1
        return max_c
