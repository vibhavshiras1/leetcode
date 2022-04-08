class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        res = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if(diff in dict1):
                res.append(i)
                res.append(dict1[diff])
                return res
            else:
                dict1[nums[i]] = i
                
                