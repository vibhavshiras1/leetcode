# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        def dfs(node,lessThan,largerThan):
            if(node is None):
                return True
            
            if(node.val<=largerThan or node.val>=lessThan):
                return False
            
            l = dfs(node.left,min(lessThan,node.val),largerThan)
            r = dfs(node.right,lessThan,max(largerThan,node.val))
            
            if(l==True and r==True):
                return True
            else:
                return False
            
        
        return dfs(root,float('inf'),float('-inf'))
    
        
            