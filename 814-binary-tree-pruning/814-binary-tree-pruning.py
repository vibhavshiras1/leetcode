# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def dfs(node):
            if(node is None):
                return False
            
            val1 = dfs(node.left)
            val2 = dfs(node.right)
            
            if(val1 is False):
                node.left = None
            
            if(val2 is False):
                node.right = None
                
            if(node.val or val1 or val2):
                return True
            else:
                return False
            
        if(dfs(root)):
            return root
        else:
            return None