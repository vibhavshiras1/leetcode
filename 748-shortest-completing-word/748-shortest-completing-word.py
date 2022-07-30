class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        dict1 = {}
        
        for i in licensePlate:
            if(i>='a' and i<='z'):
                if(i not in dict1):
                    dict1[i] = 1
                else:
                    dict1[i] += 1
            elif(i>='A' and i<='Z'):
                j = i.lower()
                if(j not in dict1):
                    dict1[j] = 1
                else:
                    dict1[j] += 1
                    
        min_len = float('inf')
        min_idx = -1
        for i in range(len(words)):
            w = words[i]
            dict2 = {}
            for key in dict1:
                dict2[key] = dict1[key]
            for j in w:
                if(j in dict2):
                    dict2[j] -= 1
                    if(dict2[j]==0):
                        dict2.pop(j)
            if(len(dict2)==0 and len(w)<min_len):
                min_len = len(w)
                min_idx = i
                
        return words[min_idx]