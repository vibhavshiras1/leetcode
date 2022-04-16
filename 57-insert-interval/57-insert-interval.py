class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        new_intervals = []
        s2 = newInterval[0]
        e2 = newInterval[1]
        count = 0
        if(len(intervals)==0):
            return [[s2,e2]]
        if(e2<intervals[0][0]):
            intervals.insert(0,newInterval)
            return intervals
        if(s2>intervals[-1][1]):
            intervals.append(newInterval)
            return intervals
        
        for i in range(len(intervals)):
            s1 = intervals[i][0]
            e1 = intervals[i][1]
            
            if(s2>=s1 and s2<=e1):
                new_s = s1
                new_e = max(e1,e2)
                new_intervals.append([new_s,new_e])
                break
            elif(s1>=s2 and s1<=e2):
                new_s = min(s1,s2)
                new_e = max(e1,e2)
                new_intervals.append([new_s,new_e])
                break
            elif(s2>e1 and e2<intervals[i+1][0]):
                new_intervals.append(intervals[i])
                new_intervals.append([s2,e2])
            else:
                new_intervals.append(intervals[i])
        
        
        for j in range(i+1,len(intervals)):
            st1 = intervals[j][0]
            en1 = intervals[j][1]
            
            if(st1>=new_intervals[-1][0] and st1<=new_intervals[-1][1]):
                new_intervals[-1][1] = max(en1,new_intervals[-1][1])
            else:
                new_intervals.append(intervals[j])
        return new_intervals
            
        