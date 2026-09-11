class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        smp = {}
        tmp = {}

        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            if s[i] in smp and smp[s[i]] != t[i]:
                return False
            if t[i] in tmp and tmp[t[i]] != s[i]:
                return False 
            smp[s[i]] = t[i]
            tmp[t[i]] = s[i]

        return True

