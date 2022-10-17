class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 1
        l = 1
        
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                l += 1
            else:
                max_len = max(max_len,l)
                l = 1
                
        max_len = max(max_len,l)
                
        return max_len