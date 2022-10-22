# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = set()
        
        def dfs(node):
            if node is None:
                return
            
            if(node.val not in s):
                s.add(node.val)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)    
        
        if(len(s)==1):
            return True
        else:
            return False