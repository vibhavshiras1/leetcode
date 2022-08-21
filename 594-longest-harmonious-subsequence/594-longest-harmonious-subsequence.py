class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        l = 0
        r = 1
        max_len = 0
        
        while(r<len(nums)):
            if(nums[r]==nums[l]+1):
                max_len = max(max_len,r-l+1)
                r += 1
                
            elif(nums[r]==nums[l]):
                r += 1
                
            else:
                while(l<r and nums[r]!=nums[l]+1):
                    l += 1
                    
                
                    
        return max_len
                