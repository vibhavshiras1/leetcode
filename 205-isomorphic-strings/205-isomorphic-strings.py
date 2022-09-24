class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        
        for i in range(len(s)):
            if(s[i] not in d):
                d[s[i]] = t[i]
            else:
                if(d[s[i]]!=t[i]):
                    return False
                
        val = set(d.values())
        
        if(len(val)!=len(d)):
            return False
                
        return True
            