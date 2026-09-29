class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for i in range(9):
            con1=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in con1:
                    return False
                con1.add(board[i][j])
        
        for i in range(9):
            con2=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                elif board[j][i] in con2:
                    return False
                con2.add(board[j][i])
        starts = [
    (0, 0), (0, 3), (0, 6),
    (3, 0), (3, 3), (3, 6),
    (6, 0), (6, 3), (6, 6)
]


        for s,c in starts:
            con3=set()
            for i in range(s,s+3):
                for j in range(c,c+3):
                    if board[i][j]==".":
                        continue
                    elif board[i][j] not in con3:
                        con3.add(board[i][j])
                    else:
                        return False
                    
        return True 

            