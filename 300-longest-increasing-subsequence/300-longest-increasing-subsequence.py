class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        
        for i in range(len(nums)-1):
            arr.append(0)
            
        arr.append(1)
        max1 = 1
        
        for i in range(len(nums)-2,-1,-1):
            max_len = 0
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    max_len = max(max_len,1+arr[j])
                else:
                    max_len = max(max_len,1)
            arr[i] += max_len
            max1 = max(max1,arr[i])
        
        return max1