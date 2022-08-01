class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        res = []
        
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        
        for i in range(k):
            res.append(d[i][0])
            
        return res