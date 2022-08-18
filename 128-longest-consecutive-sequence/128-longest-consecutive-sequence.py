class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = -1
        
        if(len(nums)==0):
            return 0
        
        s = set(nums)
            
        for num in s:
            if((num-1) not in s):
                cur_num = num
                streak = 1
                
                while((cur_num+1) in s):
                    cur_num += 1
                    streak += 1
                    
                longest = max(longest,streak)
                
        return longest