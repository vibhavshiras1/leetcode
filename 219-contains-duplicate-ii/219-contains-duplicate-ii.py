class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''[1,1,2,3]
        [0,1,1,1]
        [1,1,2,2,3,3]'''
        
        dict1 = {}
        
        for i in range(len(nums)):
            if(nums[i] not in dict1):
                dict1[nums[i]] = [i]
            else:
                if(abs(i-dict1[nums[i]][-1])<=k):
                    return True
                else:
                    dict1[nums[i]].append(i)
                
        return False