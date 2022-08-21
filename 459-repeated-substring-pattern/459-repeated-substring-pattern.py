class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        sub = ''
        
        for i in range(len(s)):
            sub += s[i]
            
            if(len(s)%len(sub)==0 and i!=len(s)-1):
                mul = len(s)//len(sub)
                if(sub*mul==s):
                    return True
                
        return False