class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        count = 0
        
        while(sum(amount)!=0):
            amount.sort()
            if(amount[1]==0):
                count += amount[2]
                amount[2] = 0
            else:
                amount[1] -= 1
                amount[2] -= 1
                count += 1
                
        return count
            