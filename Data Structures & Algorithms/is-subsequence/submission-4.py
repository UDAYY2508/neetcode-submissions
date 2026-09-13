class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        i=0
        j=0
        count = len(s)

        if len(s)>len(t):
            return False 


        while i < len(t) and j <len(s):
            if t[i] == s[j]:
                count-=1
                j+=1
            i+=1
        return count == 0
