class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        
        64 -> 16 -> 4 -> 1
        """
        
        if(n<=0):
            return False
        
        while(n>1):
            rem = n % 4
            if(rem!=0):
                return False
            n = n // 4
            
        return True
            