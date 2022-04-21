class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        max_diff = 0
        
        for i in range(len(colors)):
            for j in range(i):
                if(colors[i]!=colors[j] and (i-j)>=max_diff):
                    max_diff = (i-j)
                    
        return max_diff
            
            