class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        #  0,3     0,2 1,3     0,1 1,2 2,3     0,0 1,1 2,2        2,0
        
        
        r = 0
        c = len(mat[0]) - 1
        
        while(1):
            arr = []
            r1 = r
            c1 = c
            
            while(r1<len(mat) and c1<len(mat[0])):
                arr.append(mat[r1][c1])
                r1 += 1
                c1 += 1
                
            arr.sort()
            
            r2 = r
            c2 = c
            idx = 0
            
            while(idx<len(arr)):
                mat[r2][c2] = arr[idx]
                idx += 1
                r2 += 1
                c2 += 1
                
            if(r==0 and c==0):
                break
                
            if(c>0):
                c -= 1
            
                if(c==0):
                    r = len(mat) - 1
                    
            elif(r>=0):
                r -= 1
                
        
        return mat