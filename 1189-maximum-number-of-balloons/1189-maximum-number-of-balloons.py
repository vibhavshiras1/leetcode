class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = 0
        
        dict1 = {}
        
        for i in range(len(text)):
            if(text[i] not in dict1):
                dict1[text[i]] = 1
            else:
                dict1[text[i]] += 1
                
        str1 = "balloon"
        
        idx = 0
        
        while(idx<len(str1)):
            if(str1[idx] in dict1):
                dict1[str1[idx]] -= 1
                if(dict1[str1[idx]]==0):
                    dict1.pop(str1[idx])
                idx += 1
            else:
                break
            if(idx==len(str1)):
                count += 1
                idx = 0
                
        return count
        