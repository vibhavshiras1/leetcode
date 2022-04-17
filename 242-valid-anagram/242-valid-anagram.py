class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s)!=len(t)):
            return False
        
        dict1 = {}
        
        for i in range(len(s)):
            if(s[i] not in dict1):
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
            
            if(t[i] not in dict1):
                dict1[t[i]] = -1
            else:
                dict1[t[i]] -= 1
                
        val = dict1.values()
        
        for i in range(len(val)):
            if(val[i]!=0):
                return False
        
        return True
            
        