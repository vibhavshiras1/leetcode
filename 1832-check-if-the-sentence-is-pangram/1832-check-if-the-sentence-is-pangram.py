class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = set()
        
        for i in range(len(sentence)):
            if(sentence[i] not in s):
                s.add(sentence[i])
                
        if(len(s)==26):
            return True
        else:
            return False