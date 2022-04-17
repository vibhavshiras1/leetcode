class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        if(len(s)>12):
            return res
        
        def backtrack(idx,dots,ip):
            if(dots==4 and idx==len(s)):
                res.append(ip[:-1])
                return
            
            if(dots>4):
                return
            
            for j in range(idx,min(len(s),idx+3)):
                if(int(s[idx:j+1])<=255 and (idx==j or s[idx]!='0')):
                    backtrack(j+1,dots+1,ip+s[idx:j+1]+".")
                    
        backtrack(0,0,"")
        
        return res
        