class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict1 = {}
        
        num = [int(i) for i in num]
        
        
        for i in range(len(num)):
            if(num[i]!='0' and i in dict1):
                dict1[i] += num[i]
            elif(num[i]!='0' and i not in dict1):
                dict1[i] = num[i]
            if(num[i] not in dict1):
                dict1[num[i]] = -1
            else:
                dict1[num[i]] -= 1
            
        for key in dict1:
            if(dict1[key]!=0):
                return False
        
        return True
        