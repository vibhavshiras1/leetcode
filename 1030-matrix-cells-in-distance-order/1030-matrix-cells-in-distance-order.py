class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        dict1 = {}
        res = []
        
        for i in range(rows):
            for j in range(cols):
                dist = abs(i-rCenter) + abs(j-cCenter)
                t = (i,j)
                dict1[t] = dist
                
        s = sorted(dict1.items(), key=lambda item: item[1])
        
        for i in range(len(s)):
            res.append(list(s[i][0]))
            
        return res