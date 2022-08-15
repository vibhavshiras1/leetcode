class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        s = set(nums[0])
        
        for i in range(1,len(nums)):
            s1 = set(nums[i])
            s = s & s1
            
        l = list(s)
        
        l.sort()
        
        return l