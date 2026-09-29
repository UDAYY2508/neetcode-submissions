class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        
        for i in range(len(matrix)):
            con=set()
            for j in range(len(matrix)):
                if matrix[i][j] in con:
                    return False
                con.add(matrix[i][j])
        for i in range(len(matrix)):
            con=set()
            for j in range(len(matrix)):
                if matrix[j][i] in con:
                    return False
                con.add(matrix[j][i])
        return True
        

