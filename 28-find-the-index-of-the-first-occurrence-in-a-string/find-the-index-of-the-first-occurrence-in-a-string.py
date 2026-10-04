class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack)<len(needle) or len(haystack)==0:
            return -1
    
        l=0
        r=len(needle)

        while l<len(haystack):
            if haystack[l:r]==needle:
                return l
            l+=1
            r+=1
        return -1
        
