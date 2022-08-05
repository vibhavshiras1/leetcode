class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        # {1:(2),2:(1),1:(3),3:(1)}
        
        
        def dfs(src,target):
            if(src not in visited):
                visited.add(src)
                if(src==target):
                    return True

                for i in adj_list[src]:
                    if(dfs(i,target)==True):
                        return True
                
        
        adj_list = {}
        
        for edge in edges:
            visited = set()
            e1 = edge[0]
            e2 = edge[1]
            
            if(e1 in adj_list and e2 in adj_list and dfs(e1,e2)==True):
                return [e1,e2]
            
            if(e1 not in adj_list):
                adj_list[e1]= [e2]
            else:
                adj_list[e1].append(e2) 
            
            if(e2 not in adj_list):
                adj_list[e2] = [e1]
            else:
                adj_list[e2].append(e1)
            
            
            