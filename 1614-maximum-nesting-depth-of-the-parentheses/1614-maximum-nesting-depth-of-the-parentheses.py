class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        max_depth = 0
        
        i = 0
        
        while(i<len(s)):
            if(s[i]=='('):
                stack.append('(')
            elif(s[i]==')'):
                stack.pop()
            max_depth = max(max_depth,len(stack))
            i += 1
            
        return max_depth
        