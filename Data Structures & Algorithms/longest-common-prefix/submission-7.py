class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]
        min_len = float("inf")

        for s in strs:
            if min_len > len(s):
                min_len = len(s)


        for word in strs:
            i = 0 
            while i < len(prefix) and  i < len(word):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
                i+=1
            prefix = prefix[:min_len]
                
        return prefix

