class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        '''
        9999
          99
          98
        '''
        
        res = ''
        
        p1 = 0
        p2 = 0
        carry = 0
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        while(p1<len(num1) and p2<len(num2)):
            s = int(num1[p1]) + int(num2[p2]) + carry
            
            if(s<10):
                res += str(s)
                carry = 0
            else:
                res += str(s-10)
                carry = 1
                if(p1==len(num1)-1 and p2==len(num2)-1):
                    res += str(carry)
                
            p1 += 1
            p2 += 1
                
        
        while(p1<len(num1)):
            s = int(num1[p1]) + carry
            
            if(s>=10):
                res += str(s-10)
                carry = 1
                if(p1==len(num1)-1):
                    res += str(carry)
            else:
                res += str(s)
                carry = 0
            
            p1 += 1
            
        while(p2<len(num2)):
            s = int(num2[p2]) + carry
            
            if(s>=10):
                res += str(s-10)
                carry = 1
                if(p2==len(num2)-1):
                    res += str(carry)
            else:
                res += str(s)
                carry = 0
            
            p2 += 1
            
        
        return res[::-1]