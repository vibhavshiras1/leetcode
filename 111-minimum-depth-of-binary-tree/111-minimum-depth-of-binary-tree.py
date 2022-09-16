# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global min_depth
        min_depth = float('inf')
        
        def dfs(node,h):
            if(node is None):
                return
            
            if(node.left is None and node.right is None):
                global min_depth
                min_depth = min(min_depth,h)
            
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            
            
        dfs(root,1)
        
        if(min_depth!=float('inf')):
            return min_depth
        else:
            return 0