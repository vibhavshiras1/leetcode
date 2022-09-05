class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pos = []
        neg = []
        
        for i in range(len(nums)):
            if(nums[i]<0):
                neg.append(nums[i])
            else:
                pos.append(nums[i])
                
        p1 = 0
        p2 = 0
        
        for i in range(len(nums)):
            if(i%2==0):
                nums[i] = pos[p1]
                p1 += 1
            else:
                nums[i] = neg[p2]
                p2 += 1
                
        return nums
        