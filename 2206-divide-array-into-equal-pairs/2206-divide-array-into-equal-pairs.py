class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict1 = {}
        
        for i in range(len(nums)):
            if(nums[i] not in dict1):
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] -= 1
                if(dict1[nums[i]]==0):
                    dict1.pop(nums[i])
        
        if(len(dict1)==0):
            return True
        else:
            return False