# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global lsum
        lsum = 0
        
        def dfs(node,flag):
            if(node is None):
                return
            
            if(flag==0 and node.left is None and node.right is None):
                global lsum
                lsum += node.val
                return
            
            dfs(node.left,0)
            dfs(node.right,1)
            
        dfs(root,1)
        
        return lsum
            
        