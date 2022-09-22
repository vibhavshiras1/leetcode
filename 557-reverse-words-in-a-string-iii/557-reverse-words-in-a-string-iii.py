class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        
        res = ""
        
        for i in range(len(arr)):
            res += arr[i][::-1] + ' '
            
        res = res[:-1]
            
        
        return res