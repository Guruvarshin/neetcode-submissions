class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=set()
        c=set()
        for i in range(0,9):
            r=set()
            c=set()
            for j in range(0,9):
                if (board[i][j]!='.' and board[i][j] in r) or (board[j][i]!='.' and board[j][i] in c):
                    return False
                r.add(board[i][j])
                c.add(board[j][i])
        d=set()
        for i in range(0,9):
            d=set()
            for j in range(0,9):
                row = (i // 3) * 3 + j // 3
                col = (i % 3) * 3 + j % 3
                if board[row][col]!='.' and board[row][col] in d:
                    return False
                d.add(board[row][col])
        return True
