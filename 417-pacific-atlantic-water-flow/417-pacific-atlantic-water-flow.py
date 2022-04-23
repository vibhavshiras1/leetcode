class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])
        res = []
        
        pac = set()
        atl = set()
        
        def dfs(r,c,visit,prevH):
            if((r,c) in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c]<prevH):
                return
            
            visit.add((r,c))
            
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
        for i in range(cols):
            dfs(0,i,pac,heights[0][i])
            dfs(rows-1,i,atl,heights[rows-1][i])
            
        for i in range(rows):
            dfs(i,0,pac,heights[i][0])
            dfs(i,cols-1,atl,heights[i][cols-1])
            
        temp = pac.intersection(atl)
        
        for i in temp:
            res.append(list(i))
            
        return res