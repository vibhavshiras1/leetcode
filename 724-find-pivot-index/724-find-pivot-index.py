class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum = 0
        rsum = sum(nums) - nums[0]
        
        if(lsum==rsum):
            return 0
        
        for i in range(1,len(nums)):
            lsum+=nums[i-1]
            rsum-=nums[i]
            if(lsum==rsum):
                return i
        return -1
        