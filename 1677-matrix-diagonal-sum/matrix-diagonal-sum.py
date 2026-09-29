class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        summ=0
        n=len(mat)
        for i in range(n):
            summ += mat[i][i]
            summ += mat[i][n-1-i]

        if n%2==1:
            summ-=mat[n//2][n//2]
        return summ