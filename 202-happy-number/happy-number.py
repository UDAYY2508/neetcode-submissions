class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        summ=n
        seen = set()
        while summ !=1:
            summ = str(summ)
            total =0 
            for i in summ:
                total+=int(i)**2
                summ = total
            if summ == 1:
                return True
            elif summ in seen:
                return False
            seen.add(summ)