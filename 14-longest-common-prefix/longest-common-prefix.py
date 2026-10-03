class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        op = ""

        for i in range(len(strs[0])):
            for w in strs:
                if i>=len(w) or w[i] != strs[0][i]:
                    return op
            op+=w[i]
        return op