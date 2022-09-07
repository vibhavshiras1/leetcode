# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(node,arr):
            if(node is None):
                return []
            
            if(node.left is None and node.right is None):
                return arr + [node.val]
                
            a1 = dfs(node.left,arr)
            a2 = dfs(node.right,arr)
            
            return arr+a1+a2
            
        
        arr1 = dfs(root1,[])
        
        arr2 = dfs(root2,[])
        
        
        if(arr1==arr2):
            return True
        else:
            return False
        
        
        
