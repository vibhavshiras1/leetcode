"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        d = {}
        res = []
        
        def dfs(node,h):
            if(node is None):
                return
            
            if(h not in d):
                d[h] = [node.val]
            else:
                d[h].append(node.val)
                
            
            for i in range(len(node.children)):
                dfs(node.children[i],h+1)
                
        
        dfs(root,0)
        
        for i in range(len(d)):
            res.append(d[i])
            
        return res
        