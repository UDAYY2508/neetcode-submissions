class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True
        
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            summ=0
            for i in str(n):
                summ+=int(i)**2 
            if summ == 1:
                return True

            n=summ
        return False
            
            