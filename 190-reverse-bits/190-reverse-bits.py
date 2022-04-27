class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = 0
        p = 31
        
        while(n>0):
            t = n & 1
            n = n >> 1
            if(t==1):
                num += pow(2,p)
            p -= 1
                
        return num