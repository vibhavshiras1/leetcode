class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if(len(nums)==1):
            return
        
        lastPeak = -1
        
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                lastPeak = i
                
        if(lastPeak==-1):
            for i in range(len(nums)//2):
                nums[i],nums[n-i-1] = nums[n-i-1],nums[i]
            return
        
        idx = lastPeak
        
        for i in range(lastPeak,n):
            if(nums[i]<nums[idx] and nums[i]>nums[lastPeak-1]):
                idx = i
                
                
                
        nums[lastPeak-1],nums[idx] = nums[idx],nums[lastPeak-1]
        
        
        nums[lastPeak:n] = sorted(nums[lastPeak:n])
        