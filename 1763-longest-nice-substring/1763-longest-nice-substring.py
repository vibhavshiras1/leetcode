class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        st = -1
        end = -1
        f = 0
        
        for i in range(len(s)):
            dict1 = {}
            seen = set()
            for j in range(i,len(s)):
                if(s[j] in seen):
                    f = 1
                elif(s[j] not in dict1 and s[j].swapcase() not in dict1):
                    dict1[s[j].swapcase()] = 1
                elif(s[j] in dict1):
                    dict1.pop(s[j])
                    seen.add(s[j])
                    seen.add(s[j].swapcase())
                if(len(dict1)==0 and (j-i+1)>max_len):
                    max_len = (j-i+1)
                    st = i
                    end = j
        if(st==-1 and end==-1):
            return ""
        else:
            return s[st:end+1]
        