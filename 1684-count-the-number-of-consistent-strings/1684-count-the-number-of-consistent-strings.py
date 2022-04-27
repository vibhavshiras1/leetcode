class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        dict1 = {}
        count = 0
        
        for i in range(len(allowed)):
            if(allowed[i] not in dict1):
                dict1[allowed[i]] = 1
                
        for i in range(len(words)):
            s = words[i]
            flag = 0
            for j in s:
                if(j not in dict1):
                    flag = 1
            if(flag==0):
                count += 1
                
        return count