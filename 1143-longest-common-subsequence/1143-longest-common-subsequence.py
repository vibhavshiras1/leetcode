class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        arr = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if(text1[i]==text2[j]):
                    arr[i][j] = 1 + arr[i+1][j+1]
                else:
                    arr[i][j] = max(arr[i][j+1],arr[i+1][j])
                    
        return arr[0][0]