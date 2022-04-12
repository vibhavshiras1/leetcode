class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        grid1 = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                count = 0
                if((i-1)>=0 and board[i-1][j]==1):
                    count += 1
                if((j-1)>=0 and board[i][j-1]==1):
                    count += 1
                if((i-1)>=0 and (j-1)>=0 and board[i-1][j-1]==1):
                    count += 1
                if((i+1)<m and (j-1)>=0 and board[i+1][j-1]==1):
                    count += 1
                if((i+1)<m and board[i+1][j]==1):
                    count += 1
                if((j+1)<n and board[i][j+1]==1):
                    count += 1
                if((i+1)<m and (j+1)<n and board[i+1][j+1]==1):
                    count += 1
                if((i-1)>=0 and (j+1)<n and board[i-1][j+1]==1):
                    count += 1
                grid1[i][j] = (board[i][j],count)
                
                
        for i in range(m):
            for j in range(n):
                if(grid1[i][j][0]==1 and grid1[i][j][1]<2):
                    board[i][j] = 0
                elif(grid1[i][j][0]==1 and (grid1[i][j][1]==2 or grid1[i][j][1]==3)):
                    board[i][j] = 1
                elif(grid1[i][j][0]==1 and grid1[i][j][1]>3):
                    board[i][j] = 0
                elif(grid1[i][j][0]==0 and grid1[i][j][1]==3):
                    board[i][j] = 1
                