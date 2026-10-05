class Solution:
    def reverseWords(self, s: str) -> str:
        
        words= s.split()
        op=[]

        for w in words:
            op.append(w[::-1])

        return " ".join(op)