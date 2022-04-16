class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        def backtrack(i,cur_str):
            if(len(cur_str)==len(digits)):
                res.append(cur_str)
                return
            
            for c in letter_dict[digits[i]]:
                backtrack(i+1,cur_str+c)
        
        if(digits):
            backtrack(0,'')
        
        return res
        
        