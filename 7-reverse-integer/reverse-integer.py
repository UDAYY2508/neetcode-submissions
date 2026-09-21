class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg= True
            x = abs(x)
        
        x = list(str(x))

        l=0
        r=len(x)-1
        while l<=r:
            x[l],x[r]=x[r],x[l]
            r-=1
            l+=1
        x = int("".join(x))
        if x<-2147483648 or x>2147483647:
            return 0
        if neg:
            return -x
        return x
    

