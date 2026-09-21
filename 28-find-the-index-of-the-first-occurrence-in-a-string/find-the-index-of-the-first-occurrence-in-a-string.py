class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        count = len(needle)
        for i in range(len(haystack)):
            j=0
            k=i
            if haystack[k]==needle[j]:
                first=k
                while j<len(needle) and k<len(haystack) and haystack[k]==needle[j]:
                    k+=1
                    j+=1
                    count-=1
                if count == 0:
                    return first
                count=len(needle)
        return -1
                