class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = [nums[i] for i in range(0,len(nums),2)]
        odd = [nums[i] for i in range(1,len(nums),2)]
        
        even = sorted(even)
        
        odd = sorted(odd,reverse=True)
        
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