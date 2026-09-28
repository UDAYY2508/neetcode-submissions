class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max_=0
        for i in s:
            if i =="(":
                count+=1
            elif i ==")":
                max_=max(max_,count)
                count-=1
        return max_ 