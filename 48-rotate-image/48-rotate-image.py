class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #Transpose the matrix
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for k in range(len(matrix)):
            l = 0
            h = len(matrix[0])-1
            while(l<h):
                t = matrix[k][l]
                matrix[k][l] = matrix[k][h]
                matrix[k][h] = t
                l+=1
                h-=1