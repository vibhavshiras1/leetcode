class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = []
        
        
        stack1 = []
        stack2 = []
        
        for i in range(len(arr)):
            if(arr[i]<=x):
                stack1.append(arr[i])
            else:
                stack2.append(arr[i])
                
        
        stack2 = stack2[::-1]
        
        
        while(k>0):
            if(len(stack1)>0):
                diff1 = abs(stack1[-1] - x)
            else:
                diff1 = float('inf')
                
            if(len(stack2)>0):
                diff2 = abs(stack2[-1] - x)
            else:
                diff2 = float('inf')
                
            if(diff1<=diff2):
                res.append(stack1[-1])
                stack1.pop()
            else:
                res.append(stack2[-1])
                stack2.pop()
                
            k -= 1
            
            
        res.sort()
        return res