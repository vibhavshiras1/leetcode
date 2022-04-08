class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        a = 0
        b = 0
        c = 0
        
        for i in range(len(board)):
            row = {}
            col = {}
            box = {}
            for j in range(len(board[i])):
                if(board[i][j]!='.' and board[i][j] not in row):
                    row[board[i][j]] = 1
                elif(board[i][j] in row):
                    return False
                
                if(board[j][i]!='.' and board[j][i] not in col):
                    col[board[j][i]] = 1
                elif(board[j][i] in col):
                    return False
                
                if(board[a][b]!='.' and board[a][b] not in box):
                    box[board[a][b]] = 1
                elif(board[a][b] in box):
                    return False
                b += 1
                if(b%3==0):
                    a += 1
                    if(a==9):
                        c += 1
                        a = 0
                    else:
                        b = 3*c
                        
        return True
        
                
                        