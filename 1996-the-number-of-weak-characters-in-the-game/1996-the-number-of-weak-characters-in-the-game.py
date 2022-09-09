class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x:(-x[0],x[1]))
        
        res = 0
        max1 = 0
        
        for a,d in properties:
            if(d<max1):
                res += 1
                
            max1 = max(d,max1)
            
        return res