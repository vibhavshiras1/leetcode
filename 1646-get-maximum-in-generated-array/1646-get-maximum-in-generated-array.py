class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if(n==0):
            return 0
        
        max_num = 1
        
        arr = [0,1]
        
        for i in range(2,n+1):
            if(i%2==0):
                idx = i//2
                arr.append(arr[idx])
            else:
                idx = i//2
                arr.append(arr[idx]+arr[idx+1])
                
            max_num = max(max_num,arr[-1])
            
        return max_num