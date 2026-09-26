class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        

        mp = {k:v for k,v in knowledge}
        res = []
        curr= ""
        isbrc = False

        for c in s:
            if c=="(":
                isbrc = True
            elif c==")":
                isbrc = False
                res.append(mp.get(curr,"?"))
                curr=""
            elif isbrc:
                curr+=c
            else:
                res.append(c)
        return "".join(res)