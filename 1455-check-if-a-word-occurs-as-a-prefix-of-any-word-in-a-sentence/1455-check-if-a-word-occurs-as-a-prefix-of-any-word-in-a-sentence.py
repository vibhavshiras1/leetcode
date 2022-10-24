class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.split(' ')
        
        for i in range(len(sentence)):
            w = sentence[i]
            
            if(len(searchWord)<=len(w) and w[:len(searchWord)]==searchWord):
                return i+1
            
        return -1
                