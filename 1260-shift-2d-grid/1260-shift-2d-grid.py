class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        if(k%(m*n)==0):
            return grid
        
        grid1 = [[0 for i in range(n)] for j in range(m)]
        print(grid1)
        
        k = k % (m*n)
        
        count = 0
        i = m - (k//n)-1
        j = n - (k%n)-1
        a = 0
        b = 0
        j += 1
        if(j>=n):
            j = 0
            i += 1
        
        while(count<(m*n)):
            print(a,b,i,j)
            grid1[a][b] = grid[i][j]
            b += 1
            j += 1
            count += 1
            if(b>=n):
                b = 0
                a += 1
            if(j>=n):
                j = 0
                i += 1
                if(i>=m):
                    i = 0
                    
        return grid1
        