class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        
        a = 0
        b = 0
        nums1.sort()
        nums2.sort()
        
        while(a<len(nums1) and b<len(nums2)):
            if(nums1[a]==nums2[b]):
                res.append(nums1[a])
                a += 1
                b += 1
            elif(nums1[a]>nums2[b]):
                b += 1
            else:
                a += 1
                
        return res
        