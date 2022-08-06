# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def dfs(node,sum1,sub):
            if(node is None):
                return
            
            sub.append(node.val)
            sum1 += node.val
            
            if(node.left is None and node.right is None):
                if(sum1==targetSum):
                    res.append(sub.copy())
                    return
                
            dfs(node.left,sum1,sub.copy())
            dfs(node.right,sum1,sub.copy())
            
        dfs(root,0,[])
        
        return res