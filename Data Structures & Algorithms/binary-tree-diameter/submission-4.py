# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # allows res to be constant and not reset like a vm
        def dfs(currNode):
            if not currNode:
                return 0

            # check each leg
            left = dfs(root.left)
            right = dfs(root.right)

            # count distance with left + right
            # see if it is bigger than the record
                # first run, children to leaf nodes give 0
                # max(0, 0 + 0)
            self.res = max(self.res, left + right)

            # once present is evaluated, go up
            return 1 + max(left, right)
        
        # call function to run
        dfs(root)
        return self.res
