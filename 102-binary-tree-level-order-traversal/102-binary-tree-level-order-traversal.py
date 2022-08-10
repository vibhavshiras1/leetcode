# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        def height(node):
            if(node is None):
                return 0
            
            l = height(node.left)
            r = height(node.right)
            
            return max(l,r)+1
        
        
        def dfs(node,c):
            if(node is None):
                return
            
            res[c].append(node.val)
                
            dfs(node.left,c+1)
            dfs(node.right,c+1)
            
                
        h = height(root)
        
        for i in range(h):
            res.append([])
            
        dfs(root,0)
        
        return res
            
            