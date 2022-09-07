class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        max_alt = 0
        cur_alt = 0
        
        for i in range(len(gain)):
            cur_alt += gain[i]
            
            max_alt = max(max_alt,cur_alt)
            
        return max_alt