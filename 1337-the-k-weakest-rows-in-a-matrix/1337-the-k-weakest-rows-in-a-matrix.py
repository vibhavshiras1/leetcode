class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        res = []
        
        dict1 = {}
        
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                count += mat[i][j]
            dict1[i] = count
            
        s = sorted(dict1.items(), key=lambda item: item[1])
        print(s)
        
        i = 0
        while(i<len(s)):
            n = s[i][1]
            arr = []
            for j in range(i,len(s)):
                if(s[j][1]==n):
                    arr.append(s[j][0])
                else:
                    break
            arr.sort()
            i += len(arr)
            for row in arr:
                res.append(row)
                if(len(res)==k):
                    return res