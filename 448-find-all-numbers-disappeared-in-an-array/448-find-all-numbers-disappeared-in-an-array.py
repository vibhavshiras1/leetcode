class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        
        for i in range(1,len(nums)+1):
            dict1[i] = 1
            
        for i in range(len(nums)):
            if(nums[i] in dict1):
                dict1.pop(nums[i])
                
        res = dict1.keys()
        
        return res