class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        for i in range(9):
            con=set()
            for j in range(9):
                if board[i][j]==".":
                    continue 
                elif board[i][j] in con:
                    return False
                con.add(board[i][j])
        for i in range(9):
            con=set()
            for j in range(9):
                if board[j][i]==".":
                    continue 
                elif board[j][i] in con:
                    return False
                con.add(board[j][i])
        starts = [
    (0, 0), (0, 3), (0, 6),
    (3, 0), (3, 3), (3, 6),
    (6, 0), (6, 3), (6, 6)
]        

        for s,e in starts:
            con=set()
            for i in range(s,s+3):
                for j in range(e,e+3):
                    if board[i][j]==".":
                        continue 
                    elif board[i][j] in con:
                        return False
                    con.add(board[i][j])
        return True 


