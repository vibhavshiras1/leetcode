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
        d = {}
        
        def dfs(node,c):
            if(node is None):
                return
            
            if(c not in d):
                d[c] = [node.val]
            else:
                d[c].append(node.val)
                
            dfs(node.left,c+1)
            dfs(node.right,c+1)
                
        dfs(root,0)
        
        for i in range(len(d)):
            res.append(d[i])
            
        return res
            
            