class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = nums[0]
        max1 = nums[0]
        max_diff = 0
        
        for i in range(1,len(nums)):
            if(nums[i]<min1):
                min1 = nums[i]
                max1 = nums[i]
            elif(nums[i]>max1):
                max1 = nums[i]
                
            diff = max1 - min1
            max_diff = max(max_diff,diff)
            
        if(max_diff==0):
            return -1
        else:
            return max_diff
        