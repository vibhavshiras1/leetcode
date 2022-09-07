class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = 0
        zeros = 0
        
        for i in range(len(s)):
            if(s[i]=='0'):
                zeros += 1
            else:
                ones += 1
                
        max_score = 0
        
        l_score = 0
        r_score = ones
        
        for i in range(len(s)-1):
            if(s[i]=='0'):
                l_score += 1
            else:
                r_score -= 1
                
            max_score = max(max_score,l_score+r_score)
            
        return max_score