class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s = 0
        res = []
        
        for i in range(len(nums)):
            s += nums[i]
            res.append(s)
            
        return res