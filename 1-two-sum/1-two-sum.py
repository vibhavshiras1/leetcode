class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            ele = nums[i]
            list1 = []
            for j in range(i+1,len(nums)):
                if((ele+nums[j])==target):
                    list1.append(i)
                    list1.append(j)
                    return list1
        