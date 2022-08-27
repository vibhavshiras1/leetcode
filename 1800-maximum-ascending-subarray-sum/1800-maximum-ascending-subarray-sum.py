class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        sum1 = nums[0]
        lar = nums[0]
        
        while(idx<len(nums)):
            if(nums[idx]>nums[idx-1]):
                sum1 += nums[idx]
                if(idx==len(nums)-1):
                    lar = max(lar,sum1)
            else:
                lar = max(lar,sum1)
                sum1 = nums[idx]
            idx += 1
                
        return lar