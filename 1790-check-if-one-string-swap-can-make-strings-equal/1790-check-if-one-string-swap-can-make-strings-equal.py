class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = {}
        c = 0
        
        for i in range(len(s1)):
            if(s1[i] not in d):
                d[s1[i]] = 1
            else:
                d[s1[i]] += 1
                
        for i in range(len(s2)):
            if(s2[i] not in d):
                return False
            else:
                d[s2[i]] -= 1
                if(d[s2[i]]==0):
                    d.pop(s2[i])
                if(s2[i]!=s1[i]):
                    c += 1
                    
        if(c<=2 and len(d)==0):
            return True
        else:
            return False