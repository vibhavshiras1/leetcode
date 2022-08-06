# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if(node is None):
                return [0,True]
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            b = False
            
            if(abs(l[0]-r[0])<=1 and (l[1] and r[1])):
                b = True
            
            return [1+max(l[0],r[0]),b]
            
            
        return dfs(root)[1]
            
            