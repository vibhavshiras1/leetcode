class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        max_diff = 0
        
        p1 = 0
        p2 = len(colors) - 1
        
        while(colors[0]==colors[p2]):
            p2 -= 1
            
        while(colors[-1]==colors[p1]):
            p1 += 1
            
        
        max_diff = max(p2,len(colors)-1-p1)
                    
        return max_diff
            
            