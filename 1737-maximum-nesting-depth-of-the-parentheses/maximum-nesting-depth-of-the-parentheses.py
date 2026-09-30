class Solution:
    def maxDepth(self, s: str) -> int:
        max_=0
        dep=0
        for i in s:
            if i=="(":
                dep+=1
                max_=max(dep,max_)
            elif i==")":
                dep-=1
        return max_