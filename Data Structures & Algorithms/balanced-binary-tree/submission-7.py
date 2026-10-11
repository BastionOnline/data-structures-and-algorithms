# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                # Base case: [is_balanced, height]
                return [True, 0]

            # 1. Get results from children explicitly
            left_result = dfs(node.left)
            right_result = dfs(node.right)

            is_left_balanced = left_result[0]
            is_right_balanced = right_result[0]
            left_height = left_result[1]
            right_height = right_result[1]

            # 2. Check conditions step-by-step
            subtrees_are_balanced = is_left_balanced and is_right_balanced
            height_diff_is_valid = abs(left_height - right_height) <= 1
            
            current_balanced = subtrees_are_balanced and height_diff_is_valid
            current_height = 1 + max(left_height, right_height)

            # 3. Return the explicit package
            return [current_balanced, current_height]

        return dfs(root)[0]


# Stack Frame (or Call Stack Frame)
# The best technical term. Emphasizes that each recursive call gets its own isolated memory box on the call stack.

# Execution Frame / Activation Record
# Classic computer science synonyms for a stack frame.

# Recursive Level / Tree Depth Layer
# emphasizes the structural position in the tree rather than just the memory stack.