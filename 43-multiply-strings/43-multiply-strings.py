class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        
        if(len(num1)<len(num2)):
            t = num1
            num1 = num2
            num2 = t
            
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(len(num2)):
            n2 = int(num2[i])
            carry = 0
            sum1 = 0
            for j in range(len(num1)):
                prod = n2*int(num1[j]) + carry
                rem = prod%10
                carry = prod//10
                if(j<len(num1)-1):
                    sum1 += pow(10,j)*rem
                else:
                    sum1 += pow(10,j)*prod
            res += pow(10,i)*sum1
            
        return str(res)