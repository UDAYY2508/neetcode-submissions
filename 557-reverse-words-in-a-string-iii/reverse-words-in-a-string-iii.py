class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = s.split()
        op=[]

        for i in res:
            op.append(i[::-1])

        return " ".join(op)