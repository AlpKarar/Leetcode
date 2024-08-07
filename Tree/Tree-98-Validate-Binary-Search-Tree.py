# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, range_start = float("-inf"), range_end = float("inf")):
            if not root:
                return True
            
            if not (root.val > range_start and root.val < range_end):
                return False
            
            return (helper(root.left, range_start, root.val)
                    and helper(root.right, root.val, range_end))
        
        return helper(root)