# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # children of LEAF node have none
            # these will hit
        if not root:
            return None
        
        # swap nodes
        root.left, root.right = root.right, root.left

        # check each child nodes
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return tree after swapping
        return root