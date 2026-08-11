class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            length = str(len(word))
            encoded_string += (length+"#"+word)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            f=i
            while s[i].isdigit():
                i+= 1
            lenght = int(s[f:i])
            i+=1
            res.append(s[i:i+lenght])
            i += lenght 

        return res

            

