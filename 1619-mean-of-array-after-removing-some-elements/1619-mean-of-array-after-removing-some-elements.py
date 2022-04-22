class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        new_len = len(arr) - 0.1*len(arr)
        
        st = int(0.05*len(arr))
        end = int(len(arr)-0.05*len(arr))
        
        sum1 = sum(arr[st:end])
        
        return sum1/new_len
        