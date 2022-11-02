"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res = []
        
        def npost(node):
            
            for n in node.children:
                npost(n)
                
            res.append(node.val)
            
            
        if(root is None):
            return []
        
        npost(root)
        
        return res