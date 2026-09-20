class Solution:
    def reverseDegree(self, s: str) -> int:
        
        sum = 0
        for i in range(len(s)):
            val = 123-ord(s[i]) 
            sum+=val*(i+1)
        return sum 