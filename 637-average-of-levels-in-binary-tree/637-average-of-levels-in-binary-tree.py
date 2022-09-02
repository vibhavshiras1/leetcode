# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = {}
        res = []
        
        def dfs(node,h):
            if(node is None):
                return
            
            if(h in d):
                d[h].append(node.val)
            else:
                d[h] = [node.val]
            
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            
        dfs(root,0)
        
            
        for i in range(len(d)):
            a = d[i]
            avg = sum(a)/len(a)
            res.append(avg)
            
        return res