class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        
        for num in range(n+1):
            count = 0
            while(num>0):
                t = num % 2
                if(t==1):
                    count += 1
                num = num // 2
            ans.append(count)
            
        return ans
                
        