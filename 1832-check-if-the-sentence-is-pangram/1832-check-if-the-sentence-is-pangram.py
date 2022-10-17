class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        d = {}
        
        for i in range(len(sentence)):
            if(sentence[i] not in d):
                d[sentence[i]] = 1
                
        if(len(d)==26):
            return True
        else:
            return False