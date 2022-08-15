class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        p = 0
        l = 0
        
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                
        for i in d:
            p += d[i] // 2
            l += d[i] % 2
            
        return [p,l]