class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        
        for i in range(len(nums)):
            arr.append(1)
            
        max1 = 1
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    arr[i] = max(arr[i],1+arr[j])
            max1 = max(max1,arr[i])
        
        return max1