# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are void, they're equal
        if not p and not q:
            return True

        # one is void, not equal
        if not p or not q:
            return False

        # evaluate current node
        if p.val != q.val:
            return False

        # recursively check next node in same branch
        # return bool
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
        