"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        res = []
        
        def npre(node):
            
            res.append(node.val)
            
            for n in node.children:
                npre(n)
                
        if(root is None):
            return []
        
        npre(root)
        
        return res