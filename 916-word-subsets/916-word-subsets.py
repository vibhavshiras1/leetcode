class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        res = []
        
        for w in words2:
            dict2 = {}
            for i in w:
                if(i not in dict2):
                    dict2[i] = 1
                else:
                    dict2[i] += 1
            for key in dict2:
                if(key in dict1):
                    dict1[key].append(dict2[key])
                else:
                    dict1[key] = [dict2[key]]
                    
        for key in dict1:
            dict1[key] = max(dict1[key])
            
        for word in words1:
            dict3 = {}
            for key in dict1:
                dict3[key] = dict1[key]
            for i in word:
                if(i in dict3):
                    dict3[i] -= 1
                    if(dict3[i]==0):
                        dict3.pop(i)
            if(len(dict3)==0):
                res.append(word)
                
        return res
                