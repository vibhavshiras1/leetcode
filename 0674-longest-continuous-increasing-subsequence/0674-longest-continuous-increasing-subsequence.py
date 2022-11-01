class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        max_len = 1
        
        len1 = 1
        
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                len1 += 1
            else:
                max_len = max(max_len,len1)
                len1 = 1
                
        max_len = max(max_len,len1)
        
        return max_len