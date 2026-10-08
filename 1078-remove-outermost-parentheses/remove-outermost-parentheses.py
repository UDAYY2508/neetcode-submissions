class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        
        res=""
        dep=0

        for i in s:
            if i=="(":
                dep+=1
                if dep > 1:
                    res+=i
            elif i==")":
                dep-=1
                if dep>0:
                    res+=i
        return res

                