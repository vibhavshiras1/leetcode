class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        '''1 1 0
        1 1 0
        0 0 1
        
        {1:[2],2:[1]}'''
        
        adj = {}
        
        for i in range(len(isConnected)):
            adj[i+1] = []
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                val = isConnected[i][j]
                
                if(val==1 and i!=j):
                    adj[i+1].append(j+1)
                        
        def dfs(idx):
            if(idx in visited):
                return False
            
            visited.add(idx)
            
            for i in adj[idx]:
                dfs(i)
                
            return True
                
            
        count = 0
        visited = set()
        for i in range(1,len(isConnected)+1):
            if(dfs(i)==True):
                count += 1
            
        return count