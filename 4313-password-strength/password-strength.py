class Solution:
    def passwordStrength(self, password: str) -> int:
        password = set(password)
        op = 0
        for i in password:
            if i.islower():
                op+=1
            elif i.isupper():
                op+=2
            elif i.isdigit():
                op+=3
            else:
                op+=5
        return op