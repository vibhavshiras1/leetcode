class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        odd = []
        even = []
        
        num = str(num)
        
        for i in range(len(num)):
            if(int(num[i])%2==0):
                even.append(int(num[i]))
            else:
                odd.append(int(num[i]))
                
        odd.sort()
        even.sort()
        
        res = ""
        
        for i in range(len(num)):
            if(int(num[i])%2==0):
                res += str(even[-1])
                even.pop()
            else:
                res += str(odd[-1])
                odd.pop()
                
        return int(res)