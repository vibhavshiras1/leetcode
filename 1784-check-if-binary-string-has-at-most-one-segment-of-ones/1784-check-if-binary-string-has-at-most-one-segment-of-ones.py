class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        c = 0
        f = 0
        
        for i in range(len(s)):
            if(s[i]=='1' and f==0):
                c += 1
                f = 1
            elif(s[i]=='0' and f==1):
                f = 0
                
        if(c==1):
            return True
        else:
            return False