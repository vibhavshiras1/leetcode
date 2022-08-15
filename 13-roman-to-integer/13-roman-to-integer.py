class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"O":0}
        
        val = 0
        s+='O'
        i = 0
        while(i<len(s)-1):
            if(dict1[s[i]]<dict1[s[i+1]]):
                    val += dict1[s[i+1]]-dict1[s[i]]
                    i+=2
            else:
                val+=dict1[s[i]]
                i+=1
        return val