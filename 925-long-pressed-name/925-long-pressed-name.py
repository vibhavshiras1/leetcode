class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        a = 0
        b = 0
        
        while(a<len(name) and b<len(typed)):
            if(name[a]!=typed[b]):
                return False
            ch = name[a]
            counta = 0
            countb = 0
            
            while(a<len(name) and name[a]==ch):
                a += 1
                counta += 1
            while(b<len(typed) and typed[b]==ch):
                b += 1
                countb += 1
            if(counta>countb):
                return False
        
        if(a!=len(name) or b!=len(typed)):
            return False
        return True