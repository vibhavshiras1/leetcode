class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        res = []
        
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                
        
        d1 = {}
        
        for i in range(1,len(nums)+1):
            d1[i] = []
            
        for key in d:
            val = d[key]
            d1[val].append(key)
            
        for c in range(len(nums),0,-1):
            while(len(d1[c])>0):
                res.append(d1[c].pop())
                k -= 1
                if(k==0):
                    break
            if(k==0):
                break
                
        return res
        
        '''
        O(nlogn)
        d = {}
        res = []
        
        for i in range(len(nums)):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        print(d)
                
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        
        for i in range(k):
            res.append(d[i][0])
            
        return res'''