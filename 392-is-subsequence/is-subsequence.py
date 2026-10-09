class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        r=0
        w=0

        while w<len(s) and r<len(t):
            if s[w]==t[r]:
                w+=1
            r+=1
        return w==len(s)

