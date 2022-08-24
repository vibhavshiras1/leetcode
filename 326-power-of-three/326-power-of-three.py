class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if(n<=0):
            return False
        
        while(n>1):
            rem = n % 3
            if(rem!=0):
                return False
            n = n // 3
            
        return True