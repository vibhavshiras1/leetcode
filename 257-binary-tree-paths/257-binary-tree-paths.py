# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        res = []
        
        def dfs(node,p):
            if(node is None):
                return
            
            p += str(node.val) + "->"
            
            if(node.left is None and node.right is None):
                p = p [:-2]
                res.append(p)
                return
            
            dfs(node.left,p)
            dfs(node.right,p)
            
            
        dfs(root,"")
        
        return res