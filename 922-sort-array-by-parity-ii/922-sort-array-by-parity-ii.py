class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        
        for i in range(len(nums)):
            if(nums[i]%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
        p1 = 0
        p2 = 0
                
        for i in range(len(nums)):
            if(i%2==0):
                nums[i] = even[p1]
                p1 += 1
            else:
                nums[i] = odd[p2]
                p2 += 1
                
        return nums