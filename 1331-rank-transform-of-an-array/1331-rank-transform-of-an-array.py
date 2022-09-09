class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        d = {}
        
        sorted_arr = sorted(arr)
        
        rank = []
        
        c = 1
        
        for i in range(len(sorted_arr)):
            if(sorted_arr[i] not in d):
                d[sorted_arr[i]] = c
                c += 1
                
        for i in range(len(arr)):
            rank.append(d[arr[i]])
            
        
        return rank