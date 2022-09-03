# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            
            if(node.left is None and node.right is None):
                return node.val
            
            val1 = dfs(node.left)
            val2 = dfs(node.right)
            
            if(node.val==2):
                return (val1 or val2)
            else:
                return (val1 and val2)
            
            
        return dfs(root)