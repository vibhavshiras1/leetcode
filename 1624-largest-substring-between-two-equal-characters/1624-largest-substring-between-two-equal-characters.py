class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = -1
        
        d = {}
        
        for i in range(len(s)):
            if(s[i] in d):
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
                
                
        for c in d:
            l = d[c]
            
            if(len(l)>=2):
                len1 = l[-1] - l[0] - 1
                max_len = max(max_len,len1)
                
        
        return max_len