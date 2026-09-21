class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        add = ""
        res=[]
        for i in digits:
            add+=str(i)
        add = int(add)
        summ=add+1
        for dig in str(summ):
            sin = int(dig)
            res.append(sin)
        return res


