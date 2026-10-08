# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # create instance variable
        self.res = 0

        # allows res to be constant and not reset like a vm
            # maintains state across recursive call stack frames
        def dfs(currNode):
            if not currNode:
                return 0

            # check each leg
            left = dfs(currNode.left)
            right = dfs(currNode.right)

            # count distance with left + right
                # this is the diameter
            # see if it is bigger than the record
                # first run, children to leaf nodes give 0
                # max(0, 0 + 0)
            self.res = max(self.res, left + right)

            # compute height of this current subtree, give to parent
                # 1 for current node + longer leg to pass to parent
            return 1 + max(left, right)
        
        # call function to run
        dfs(root)

        # return updated result
        return self.res
