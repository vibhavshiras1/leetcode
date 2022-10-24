class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        c = 0
        
        for i in range(len(words)):
            w = words[i]
            
            if(len(w)<=len(s) and w==s[:len(w)]):
                c += 1
                
        return c