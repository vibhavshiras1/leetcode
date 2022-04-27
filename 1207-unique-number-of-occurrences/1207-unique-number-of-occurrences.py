class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        
        dict1 = {}
        
        num = arr[0]
        count = 1
        
        for i in range(1,len(arr)):
            if(arr[i]==num):
                count += 1
            else:
                if(count not in dict1):
                    dict1[count] = 1
                    count = 1
                    num = arr[i]
                else:
                    return False
            if(i==len(arr)-1):
                if(count in dict1):
                    return False
                     
        return True