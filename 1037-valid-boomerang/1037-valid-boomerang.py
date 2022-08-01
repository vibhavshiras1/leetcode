class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dict1 = {}
        
        for point in points:
            t = tuple(point)
            if(t not in dict1):
                dict1[t] = 1
            else:
                return False
        
        try:
            slope1 = (points[1][1] - points[0][1])/(points[1][0] - points[0][0])
        except:
            slope1 = float('inf')
        try:
            slope2 = (points[2][1] - points[0][1])/(points[2][0] - points[0][0])
        except:
            slope2 = float('inf')
        try:        
            slope3 = (points[2][1] - points[1][1])/(points[2][0] - points[1][0])
        except:
            slope3 = float('inf')
        
        
        if(slope1==slope2 or slope2==slope3 or slope1==slope3):
            return False
        else:
            return True