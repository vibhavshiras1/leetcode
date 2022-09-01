# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global count
        count = 0
        
        def dfs(node,maxv):
            if(node is None):
                return
            
            if(node.val >= maxv):
                global count
                count += 1
                maxv = node.val
            
            dfs(node.left,maxv)
            dfs(node.right,maxv)
            
        
        dfs(root,float('-inf'))
        
        return count