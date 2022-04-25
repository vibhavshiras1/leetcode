class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        words = text.split(' ')
        s = first + second
        
        for i in range(len(words)-2):
            w = words[i] + words[i+1]
            if(w==s):
                res.append(words[i+2])
        
        return res
                
            
        