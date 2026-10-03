class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        i=len(s)-1
        while i>=0:
            if s[i]!=" ":
                r=i
                while r>=0 and s[r]!=" ":
                    r-=1
                word = s[r+1:i+1]
                res.append(word)
                i=r
            i-=1
        return " ".join(res)
