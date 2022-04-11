class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        
        a = 0
        b = 0
        count = 0
        
        while(a<len(word1) and b<len(word2)):
            if(count%2==0):
                res += word1[a]
                a += 1
            else:
                res += word2[b]
                b += 1
            count += 1
                
        if(a<len(word1)):
            res += word1[a:]
        elif(b<len(word2)):
            res += word2[b:]
            
        return res