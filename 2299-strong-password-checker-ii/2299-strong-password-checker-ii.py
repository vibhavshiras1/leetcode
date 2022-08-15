class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        c1 = False
        c2 = False
        c3 = False
        c4 = False
        c5 = False
        c6 = True
        
        if(len(password)>=8):
            c1 = True
        
        for i in range(len(password)):
            if(password[i].islower()):
                c2 = True
            elif(password[i].isupper()):
                c3 = True
            elif(password[i].isdigit()):
                c4 = True
            elif(password[i] in "!@#$%^&*()-+"):
                c5 = True
            
            if(i<len(password)-1 and password[i]==password[i+1]):
                c6 = False
                
        if(c1 and c2 and c3 and c4 and c5 and c6):
            return True
        else:
            return False