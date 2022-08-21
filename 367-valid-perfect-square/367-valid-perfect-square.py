import math

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = num
        
        while(l<=r):
            mid = l + (r-l)//2
            
            if(mid**2==num):
                return True
            
            if(mid**2>num):
                r = mid - 1
            else:
                l = mid + 1
                
        return False