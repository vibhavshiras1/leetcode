class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict1 = {}
        
        for i in range(len(t)):
            if(t[i] not in dict1):
                dict1[t[i]] = 1
            else:
                dict1[t[i]] += 1
                
        for i in range(len(s)):
            if(s[i] in dict1):
                dict1[s[i]] -= 1
                if(dict1[s[i]]==0):
                    dict1.pop(s[i])
                    
        for i in dict1:
            return i
        