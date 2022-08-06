class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        f = 0
        
        for i in range(1,len(s)):
            if(s[i]=='0'):
                f = 1
            elif(s[i]=='1' and f==1):
                return False
                
        return True