class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        
        res = ''
        
        if(len(s)==0):
            return 0
        
        i = 0
        
        if(s[i]=='-' or s[i]=='+'):
            res += s[i]
            i += 1
            
        while(i<len(s)):
            if(s[i].isdigit()):
                res += s[i]
            else:
                break
            i += 1
        
        if(len(res)!=0 and res[-1].isdigit()):
            res = int(res)
        else:
            res = 0
        
        if(res>=pow(2,31)):
            res = pow(2,31) - 1
        elif(res<pow(-2,31)):
            res = pow(-2,31)
            
        return res
            
        