class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]    [5,8,8,8,10,11,12]
        """
        res = []
        
        
        l = 0
        r = len(nums)-1
        lcount = 0
        rcount = 0
        
        while(l<=r and len(res)<2):
            if(nums[l]==target and lcount==0):
                res.append(l)
                lcount+=1
            elif(nums[l]!=target and lcount==0):
                l+=1
            if(nums[r]==target and rcount==0):
                res.append(r)
                rcount+=1
            elif(nums[r]!=target and rcount==0):
                r-=1
        if(len(res)==0):
            return [-1,-1]
        if(res[0]>res[1]):
            tmp = res[0]
            res[0] = res[1]
            res[1] = tmp
        return res
            
        
        
        