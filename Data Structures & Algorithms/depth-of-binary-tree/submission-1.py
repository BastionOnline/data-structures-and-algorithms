# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxCount = 0
        count = 0

        if not root:
            count -=1
            return None
        
        count +=1
        maxCount = max(count, maxCount)

        self.maxDepth(root.left)
        self.maxDepth(root.right)

        return maxCount