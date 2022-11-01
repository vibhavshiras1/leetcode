class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum1 = 0
        
        for i in range(k):
            sum1 += nums[i]
            
        max_avg = sum1 / k
        
        for i in range(k,len(nums)):
            sum1 += nums[i]
            sum1 -= nums[i-k]
            max_avg = max(max_avg,sum1/k)
            
        return max_avg