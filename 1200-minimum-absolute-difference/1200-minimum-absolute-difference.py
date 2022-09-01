class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res = []
        min_diff = float('inf')
        
        arr.sort()
        
        for i in range(1,len(arr)):
            diff = abs(arr[i] - arr[i-1])
            
            sub = [arr[i-1],arr[i]]
            
            if(diff==min_diff):
                res.append(sub)
                
            elif(diff<min_diff):
                min_diff = diff
                res = []
                res.append(sub)
                
        return res