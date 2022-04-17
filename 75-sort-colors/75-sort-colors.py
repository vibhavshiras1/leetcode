class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        idx = 0
        
        while(idx<=end and start<end):
            if(nums[idx]==0):
                nums[idx] = nums[start]
                nums[start] = 0
                start += 1
                idx += 1
            elif(nums[idx]==2):
                nums[idx] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                idx += 1
        
        