class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        
        d = {}
        
        for i in range(len(arr)):
            if(arr[i] not in d):
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1
        
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        
        c = 0
        
        for i in range(len(d)):
            n -= d[i][1]
            c += 1
            if(n<=len(arr)//2):
                break
                
        return c