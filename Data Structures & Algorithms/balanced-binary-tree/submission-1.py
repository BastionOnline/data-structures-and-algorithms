# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(currNode):
            if not currNode:
                return 0
            
            left = dfs(currNode.left)
            right = dfs(currNode.right)

            return 1 + max(left, right)

        
        left, right = dfs(root.left), dfs(root.right)

        difference = max(left, right) - min(left, right)
            
        return True if difference == 1 else False