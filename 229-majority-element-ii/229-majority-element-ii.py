class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                
        for num in d:
            if(d[num]>len(nums)//3):
                res.append(num)
                
        return res