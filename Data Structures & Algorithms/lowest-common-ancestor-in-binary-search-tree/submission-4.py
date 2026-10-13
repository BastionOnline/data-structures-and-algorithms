# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # left of node is lower values
        # right of node is higher values

        cur = root

        while cur:
            # if cur is less than p and q, go right
            # p is higher val than cur
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # if cur is greater than p and q, go left
            # p is lower val than cur
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            # if it is not lower, or greater, this is the LCA
                # Lowest Common Ancestor
            else:
                return cur