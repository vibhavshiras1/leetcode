class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        res = ''
        c = 0
        temp = 0
        
        if(len(s)<=k):
            return s
        
        while(1):
            for i in range(len(s)):
                c += 1
                temp += int(s[i])
                if(c==k):
                    res += str(temp)
                    temp = 0
                    c = 0
            if(c<k and c!=0):
                res += str(temp)
                temp = 0
                c = 0
            print(res)
            if(len(res)>k):
                s = res
                res = ''
            else:
                break
                
        return res
                
        