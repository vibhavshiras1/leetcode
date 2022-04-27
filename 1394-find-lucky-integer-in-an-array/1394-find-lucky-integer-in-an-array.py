class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict1 = {}
        max_val = -1
        
        for i in range(len(arr)):
            if(arr[i] in dict1):
                dict1[arr[i]] += 1
            else:
                dict1[arr[i]] = 1
                
        for i in dict1:
            if(dict1[i]==i and i>max_val):
                max_val = i
                
        return max_val
        