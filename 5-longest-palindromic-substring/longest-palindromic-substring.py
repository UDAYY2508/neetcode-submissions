class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s==s[::-1]:
            return s 

        longest=0
        res=s[0]
        
        for l in range(len(s)):
            for r in range(l+1,len(s)):
                if s[l]==s[r]:
                    curr = s[l:r+1]
                    if curr==curr[::-1] and len(curr)>longest:
                        res = curr
                        longest=len(curr)
        
        return res
                     
                    




