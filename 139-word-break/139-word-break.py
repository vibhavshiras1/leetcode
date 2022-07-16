class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if((i+len(w))<=len(s) and s[i:i+len(w)]==w):
                    dp[i] = dp[i+len(w)]
                if(dp[i]==True):
                    break
                    
        return dp[0]
        
        
        '''
        brute force
        
        def backtrack(idx):
            if(idx==len(s)):
                return True
            
            for i in range(len(wordDict)):
                len1 = len(wordDict[i])
                if((idx+len1)<=len(s) and s[idx:idx+len1]==wordDict[i]):
                    if(backtrack(idx+len1)):
                        return True
                
            return False
                
        return backtrack(0)'''
        
        