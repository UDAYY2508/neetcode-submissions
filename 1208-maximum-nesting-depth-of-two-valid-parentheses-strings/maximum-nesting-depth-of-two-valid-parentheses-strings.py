class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans=[]
        dep=0
        for c in seq:
            if c=="(":
                dep+=1
                ans.append(dep % 2)
            else:
                ans.append(dep % 2)
                dep-=1
        return ans