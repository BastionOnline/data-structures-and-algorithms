# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this is comparing root to subroot
        # main goal to identify the top head node

        # root does not exist, cant compare, False
        if not root: return False

        # subroot is null, root leaf children are null, True
        if not subRoot: return True

        # both nodes exist
        # check for match STARTING at current node
        # Brute Force check
            # if case is active if function returns True
        if self.isSameTree(root, subRoot):
            return True

        # current node doesn't match
        # subtree could deep inside the main tree
        # do this again checking each child
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    def isSameTree(self, root, subRoot):
        # both nodes dont exist in the list
        if not root and not subRoot:
            return True
        
        # both nodes exist and the values are thes same
        # check both children
        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and
                    (self.isSameTree(root.right, subRoot.right)))

        # one node is missing
        return False